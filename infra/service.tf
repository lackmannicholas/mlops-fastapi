provider "aws" {
    region = "us-west-2"
}

resource "aws_ecs_cluster" "example" {
    name = "example-cluster"
}

resource "aws_ecs_task_definition" "example" {
    family                   = "example-task"
    network_mode             = "awsvpc"
    requires_compatibilities = ["FARGATE"]
    cpu                      = "256"
    memory                   = "512"

    container_definitions = jsonencode([
        {
            name      = "example-app"
            image     = "nginx:latest"
            essential = true
            portMappings = [
                {
                    containerPort = 80
                    hostPort      = 80
                }
            ]
        }
    ])
}

resource "aws_ecs_service" "example" {
    name            = "example-service"
    cluster         = aws_ecs_cluster.example.id
    task_definition = aws_ecs_task_definition.example.arn
    desired_count   = 1
    launch_type     = "FARGATE"

    network_configuration {
        subnets         = ["subnet-0123456789abcdef0"]
        security_groups = ["sg-0123456789abcdef0"]
    }
}