#!/bin/bash

# Ubuntu System Update Script
# Author: [Your Name]

echo "Starting system update..."

# Update package lists
sudo apt update

# Upgrade system packages
sudo apt upgrade -y

# Remove unnecessary packages
sudo apt autoremove -y

# Clean up cache
sudo apt autoclean

echo "System update completed!"

