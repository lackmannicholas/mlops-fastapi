# resource "aws_ecs_task_definition" "task_definition" {
#     family                   = "mlops-fastapi"
#     network_mode             = "awsvpc"
#     requires_compatibilities = ["FARGATE"]
#     cpu                      = "256"
#     memory                   = "512"
#     container_definitions = jsonencode([
#         {
#             name      = "nginx"
#             image     = "nginx:latest"
#             essential = true
#             portMappings = [
#                 {
#                     containerPort = 80
#                     hostPort      = 80
#                 }
#             ]
#         }
#     ])
# }

# resource "aws_ecs_service" "ecs_service" {
#     name            = "mlops-fastapi"
#     cluster         = aws_ecs_cluster.ecs_cluster.id
#     task_definition = aws_ecs_task_definition.task_definition.arn
#     desired_count   = 1
#     launch_type     = "FARGATE"

#     network_configuration {
#         subnets         = ["subnet-0123456789abcdef0"]
#         security_groups = ["sg-0123456789abcdef0"]
#     }
# }