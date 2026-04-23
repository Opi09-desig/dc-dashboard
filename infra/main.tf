provider "aws" {
  region = "us-east-1"
}

# 1. Repositorio donde subiremos el Docker
resource "aws_ecr_repository" "repo" {
  name                 = "dc-dashboard-repo"
  force_delete         = true
}

# 2. El "Cerebro" (Cluster ECS)
resource "aws_ecs_cluster" "main" {
  name = "dc-ops-cluster"
}

# 3. El Load Balancer (El que te da el LINK)
resource "aws_lb" "main" {
  name               = "dc-ops-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.lb_sg.id]
  subnets            = data.aws_subnets.default.ids
}

# --- Recursos de Red (Configuración automática) ---
data "aws_vpc" "default" { default = true }
data "aws_subnets" "default" {
  filter { 
    name = "vpc-id"
    values = [data.aws_vpc.default.id]
    }
}

resource "aws_security_group" "lb_sg" {
  name        = "allow_streamlit"
  description = "Allow Streamlit inbound traffic"
  vpc_id      = data.aws_vpc.default.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# 4. Output: ESTO TE DARÁ EL LINK EN LA TERMINAL
output "alb_dns_name" {
  value = "http://${aws_lb.main.dns_name}"
}