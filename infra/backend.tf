terraform {
    backend "s3" {
        bucket         = "terraform-mlops-fastapi"
        key            = "mlops-fastapi"
        region         = "us-east-1"
    }
}