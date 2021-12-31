variable "lambda_function_name" {
  type        = string
  default     = "utility-costs-notifier"
  description = "Lambda funtion name"
}

variable "deployment_package_bucket" {
  type        = string
  description = "S3 bucket name for Lambda deploy resources"
}

variable "deployment_package_key" {
  type        = string
  description = "Key of deploy resources in deployment_package_bucket"
}

variable "cloudwatch_event_rule_name" {
  type        = string
  default     = "utility-costs-monthly-report"
  description = "Cloudwatch Event Rule name"
}

variable "cloudwatch_event_schedule_expression" {
  type        = string
  default     = "cron(0 3 1 * ? *)"
  description = "Schedule expression for Cloudwatch Event(Cron or Rate)"
}

variable "line_notify_token_parameter_name" {
  type        = string
  default     = "line-notify-token"
  description = "Parameter name of Systems Manager Parameter Store for LINE Notify token"
}

data "aws_caller_identity" "current" {}

data "aws_region" "current" {}
