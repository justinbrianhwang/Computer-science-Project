# System Update and Configuration Guide

This guide provides step-by-step instructions for system updates, package installations, user account setups, network configurations, security settings, and other essential configurations for Debian/Ubuntu and Red Hat/CentOS systems.

## System Update

### Debian/Ubuntu:
sudo apt update && sudo apt upgrade -y

### Red Hat/CentOS:
sudo yum update -y
Package Installation

### Debian/Ubuntu:
sudo apt install build-essential curl wget vim git -y

### Red Hat/CentOS:
sudo yum groupinstall "Development Tools" -y
sudo yum install curl wget vim git -y

## User Account and Permissions
Add a New User:
sudo adduser <username>
sudo passwd <username>

## Grant sudo Privileges:
### Debian/Ubuntu:
sudo usermod -aG sudo <username>
### Red Hat/CentOS:
sudo usermod -aG wheel <username>
Network Configuration
Set Static IP (if needed):
Modify /etc/network/interfaces or /etc/netplan/*.yaml for Debian/Ubuntu.
Use nmtui or nmcli for Red Hat/CentOS.
Security Settings
# Install and Configure SSH:

## Install SSH:

### Debian/Ubuntu:
sudo apt install openssh-server -y

### Red Hat/CentOS:
sudo yum install openssh-server -y

## Restart SSH:
### Debian/Ubuntu:
sudo systemctl restart ssh
### Red Hat/CentOS:
sudo systemctl restart sshd

## Firewall Configuration:
### UFW (Debian/Ubuntu):
sudo apt install ufw -y
sudo ufw enable
sudo ufw allow ssh
sudo ufw status

### Firewalld (Red Hat/CentOS):
sudo yum install firewalld -y
sudo systemctl start firewalld
sudo systemctl enable firewalld
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
sudo firewall-cmd --list-all

## Install and Configure Fail2Ban:
### Debian/Ubuntu:
sudo apt install fail2ban -y

### Red Hat/CentOS:
sudo yum install epel-release -y && sudo yum install fail2ban -y
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
System Monitoring Tools

## Install htop:
sudo apt install htop -y
sudo yum install htop -y
Timezone and Hostname Configuration

## Set Timezone:
sudo timedatectl set-timezone <your-timezone>

## Set Hostname:
sudo hostnamectl set-hostname <new-hostname>

# Swap Memory Configuration (if needed)
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

## Install VI/Vim
### Debian/Ubuntu:
sudo apt update
sudo apt install vim -y
### Red Hat/CentOS:
sudo yum install vim -y
