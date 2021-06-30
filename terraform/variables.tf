variable "cloudwatch_group" {
  type = string
  default = "booking-service"
}

variable "name_prefix" {
  description = "Name prefix of each resources"
  type = string
  default = "booking-service"
}

variable "IMAGE_VERSION" {
  type = string
}

variable "VACCINE_LINE_TOKEN" {
  type = string
  default = "vaccine_line_token"
}
