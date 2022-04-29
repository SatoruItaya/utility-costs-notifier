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

variable "mail_address_parameter_name" {
  type        = string
  default     = "mail-address"
  description = "Parameter name of Systems Manager Parameter Store for mail address"
}

variable "mail_address_parameter_name" {
  type        = string
  default     = "mail-address"
  description = "Parameter name of Systems Manager Parameter Store for mail address"
}

variable "tokyo_gas_password_parameter_name" {
  type        = string
  default     = "tokyo-gas-password"
  description = "Parameter name of Systems Manager Parameter Store for Tokyo Gas password"
}

variable "tokyo_suido_id_parameter_name" {
  type        = string
  default     = "tokyo-suido-id"
  description = "Parameter name of Systems Manager Parameter Store for Tokyo Suido ID"
}

variable "tokyo_suido_password_parameter_name" {
  type        = string
  default     = "tokyo-suido-password"
  description = "Parameter name of Systems Manager Parameter Store for Tokyo Suido password"
}

variable "next_power_id_parameter_name" {
  type        = string
  default     = "next-power-id"
  description = "Parameter name of Systems Manager Parameter Store for Next Power ID"
}

variable "next_power_password_parameter_name" {
  type        = string
  default     = "next-power-password"
  description = "Parameter name of Systems Manager Parameter Store for Next Power password"
}

data "aws_caller_identity" "current" {}

data "aws_region" "current" {}
