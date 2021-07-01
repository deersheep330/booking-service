[
  {
    "essential": true,
    "name": "booking-container",
    "memory": 256,
    "cpu": 128,
    "image": "${image}",
    "environment": [
      { "name": "VACCINE_LINE_TOKEN", "value": "${vaccine_line_token}" }
    ],
    "logConfiguration": {
      "logDriver": "awslogs",
      "options": {
        "awslogs-group": "${awslogs_group}",
        "awslogs-region": "${awslogs_region}",
        "awslogs-stream-prefix": "${awslogs_prefix}"
      }
    }
  }
]