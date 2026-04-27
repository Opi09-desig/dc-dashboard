output "alb_dns_name" {
  description = "URL pública del Dashboard"
  value       = aws_lb.main.dns_name
}

output "ecr_repository_url" {
  description = "URL del repositorio ECR"
  value       = aws_iam_role.ecs_task_execution_role.arn
}