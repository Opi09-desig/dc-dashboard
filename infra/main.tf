provider "aws" {
  region = "us-east-1" # <--- Asegúrate de que diga esto exactamente
}

# --- VPC y Red ---
resource "aws_vpc" "main_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  tags = { Name = "dc-ops-vpc" }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main_vpc.id
  tags   = { Name = "dc-ops-igw" }
}

resource "aws_subnet" "public_subnets" {
  count                   = 2
  vpc_id                  = aws_vpc.main_vpc.id
  cidr_block              = "10.0.${count.index + 1}.0/24"
  availability_zone       = count.index == 0 ? "us-east-1a" : "us-east-1b"
  map_public_ip_on_launch = true # Vital para que los servicios tengan salida
  tags = { Name = "dc-ops-public-subnet-${count.index + 1}" }
}

resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.main_vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }
}

resource "aws_route_table_association" "public_assoc" {
  count          = 2
  subnet_id      = aws_subnet.public_subnets[count.index].id
  route_table_id = aws_route_table.public_rt.id
}

# --- Security Groups ---
resource "aws_security_group" "ecs_sg" {
  name        = "dc-ops-ecs-sg"
  description = "Allow inbound 8501 and outbound for ECR"
  vpc_id      = aws_vpc.main_vpc.id

  ingress {
    from_port   = 8501
    to_port     = 8501
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Permitir ver el Dashboard
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"] # Vital para descargar la imagen de ECR
  }
}

# --- ECS Cluster y Service ---
resource "aws_ecs_cluster" "dc_cluster" {
  name = "dc-ops-cluster"
}

resource "aws_ecs_task_definition" "dc_task" {
  family                   = "dc-ops-task"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn

  container_definitions = jsonencode([{
    name      = "dc-dashboard-container"
    image     = "974125292218.dkr.ecr.us-east-1.amazonaws.com/dc-dashboard-repo:latest"
    essential = true
    portMappings = [{
      containerPort = 8501
      hostPort      = 8501
    }]
  }])
}

resource "aws_ecs_service" "dc_service" {
  name            = "dc-ops-service-v2"
  cluster         = aws_ecs_cluster.dc_cluster.id
  task_definition = aws_ecs_task_definition.dc_task.arn
  launch_type     = "FARGATE"
  desired_count   = 1

  network_configuration {
    subnets          = aws_subnet.public_subnets[*].id
    security_groups  = [aws_security_group.ecs_sg.id]
    assign_public_ip = true # SOLUCIÓN AL TIMEOUT: Permite a Fargate descargar la imagen
  }
}

# --- IAM Role (Identidad del Servidor) ---
resource "aws_iam_role" "ecs_task_execution_role" {
  name = "ecsTaskExecutionRoleV4"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = { Service = "ecs-tasks.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "ecs_execution_attachment" {
  role       = aws_iam_role.ecs_task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}