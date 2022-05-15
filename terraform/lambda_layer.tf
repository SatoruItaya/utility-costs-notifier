locals {
  headless_chromium_url = "https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-55/stable-headless-chromium-amazonlinux-2.zip"
}

resource "null_resource" "headless_chromium" {
  provisioner "local-exec" {
    command = "curl -SL ${local.headless_chromium_url} > headless-chromium.zip"
  }
}

resource "aws_s3_object" "headless_chromium" {
  bucket = var.deployment_package_bucket
  key    = "layer/headless-chromium.zip"
  source = "headless-chromium.zip"

  etag = filemd5("headless-chromium.zip")

  depends_on = [null_resource.headless_chromium]
}

resource "aws_lambda_layer_version" "headless_chromium" {
  layer_name               = "headless-chromium"
  s3_bucket                = aws_s3_object.headless_chromium.bucket
  s3_key                   = aws_s3_object.headless_chromium.key
  compatible_runtimes      = ["python3.7"]
  compatible_architectures = ["x86_64"]
}
