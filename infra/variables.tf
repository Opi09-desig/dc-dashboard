variable "aws_region" {
  description = "Región de AWS para el despliegue"
  default     = "us-east-1"
}

variable "project_name" {
  description = "Nombre del proyecto"
  default     = "dc-ops-piscina"
}

variable "ecr_repository_name" {
  description = "Nombre del repositorio en ECR"
  default     = "dc-dashboard-repo"
}