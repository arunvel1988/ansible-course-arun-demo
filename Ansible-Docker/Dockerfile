FROM ubuntu:20.04

# Install Ansible and necessary packages
RUN apt-get update && \
    apt-get install -y ansible python3-pip sshpass openssh-client && \
    apt-get clean

# Create an Ansible directory
WORKDIR /ansible



