#!/bin/bash

# Prompt for the recipient email address.
read -p "Enter recipient email address: " recipient

# Prompt for the sender email address.
read -p  "Enter sender email address: "  sender

# Prompt for the email subject.
read -p "Enter email subject: " subject

# Prompt for the email body.
echo "Enter email body (end with an empty line): "
body=""
while IFS= read -r line; do
    [ -z "$line" ] && break
    body="$body$line\n"
done

# Send the email.
echo -e "$body" | mail -s "$subject" -a "From: $sender" "$recipient"

echo "Email sent from $sender to $recipient"
