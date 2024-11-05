resource "aws_apprunner_service" "mlops_fastapi_service" {
    service_name = "mlops-fastapi-service"

    source_configuration {
        authentication_configuration {
            connection_arn = aws_apprunner_connection.example.arn
        }

        auto_deployments_enabled = true

        image_repository {
            image_identifier      = "${aws_ecr_repository.mlops_fastapi.repository_url}:latest"
            image_repository_type = "ECR"
        }
    }

    instance_configuration {
        cpu    = "1024"
        memory = "2048"
    }

    tags = {
        Name = "mlops-fastapi"
    }
}

resource "aws_apprunner_connection" "example" {
    connection_name = "github-connection"

    provider_type = "GITHUB"

    tags = {
        Name = "github-connection"
    }
}