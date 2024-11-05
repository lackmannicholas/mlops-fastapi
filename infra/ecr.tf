resource "aws_ecr_repository" "mlops_fastapi" {
    name                 = "mlops-fastapi"
    image_tag_mutability = "MUTABLE"
    image_scanning_configuration {
        scan_on_push = true
    }
    tags = {
        Name = "mlops-fastapi"
    }
}