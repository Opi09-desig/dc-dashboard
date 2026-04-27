output "ecs_cluster_name" {
  value = aws_ecs_cluster.dc_cluster.name
}

output "ecs_service_name" {
  value = aws_ecs_service.dc_service.name
}