provider "aws" {
  region = ""
  #Go to IAM to find access key & secret key
  access_key = ""
  secret_key = ""
}

resource "aws_instance" "TF-Test" {
  ami = "ami-085925f297f89fce1"
  instance_type = "t2.micro"
}

# resource "<provider>_<resource_type>" "name" {
#   config options...
#   key = ""
# }