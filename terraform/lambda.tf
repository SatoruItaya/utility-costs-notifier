resource "aws_lambda_function" "lambda" {
  function_name = var.lambda_function_name
  handler       = "lambda_function.lambda_handler"
  role          = aws_iam_role.lambda_iam_role.arn

  runtime = "python3.7"

  s3_bucket = var.deployment_package_bucket
  s3_key    = var.deployment_package_key

  timeout = 60

  environment {
    variables = {
      LINE_NOTIFY_TOKEN_PARAMETER_NAME    = var.line_notify_token_parameter_name
      MAIL_ADDRESS_PARAMETER_NAME         = var.mail_address_parameter_name
      TOKYO_GASS_PASSWORD_PARAMETER_NAME  = var.tokyo_gas_password_parameter_name
      TOKYO_SUIDO_ID_PARAMETER_NAME       = var.tokyo_suido_id_parameter_name
      TOKYO_SUIDO_PASSWORD_PARAMETER_NAME = var.tokyo_suido_password_parameter_name
      NEXT_POWER_ID_PARAMETER_NAME        = var.next_power_id_parameter_name
      NEXT_POWER_PASSWORD_PARAMETER_NAME  = var.next_power_password_parameter_name
    }
  }
}

resource "aws_cloudwatch_log_group" "lambda_log_group" {
  name              = "/aws/lambda/${var.lambda_function_name}"
  retention_in_days = 3
}

resource "aws_cloudwatch_log_stream" "lambda_log_stream" {
  name           = var.lambda_function_name
  log_group_name = aws_cloudwatch_log_group.lambda_log_group.name
}

resource "aws_iam_role" "lambda_iam_role" {
  name = var.lambda_function_name

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_iam_policy" "lambda_iam_policy" {
  name        = var.lambda_function_name
  path        = "/"
  description = "IAM policy for logging from ${var.lambda_function_name}"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "${aws_cloudwatch_log_group.lambda_log_group.arn}:*",
      "Effect": "Allow"
    },
    {
      "Action": "ssm:GetParameter",
      "Resource": [
        "arn:aws:ssm:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:parameter/${var.line_notify_token_parameter_name}",
        "arn:aws:ssm:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:parameter/${var.mail_address_parameter_name}",
        "arn:aws:ssm:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:parameter/${var.tokyo_gas_password_parameter_name}",
        "arn:aws:ssm:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:parameter/${var.tokyo_suido_id_parameter_name}",
        "arn:aws:ssm:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:parameter/${var.tokyo_suido_password_parameter_name}",
        "arn:aws:ssm:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:parameter/${var.next_power_id_parameter_name}",
        "arn:aws:ssm:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:parameter/${var.next_power_password_parameter_name}"
      ],
      "Effect": "Allow"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "lambda_iam_role_policy_attachment" {
  role       = aws_iam_role.lambda_iam_role.name
  policy_arn = aws_iam_policy.lambda_iam_policy.arn
}
