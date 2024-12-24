#!/bin/bash

# Prompt for the recipient email address.
read -p "Enter recipient email address: " recipient

# Prompt for the sender email address.
read -p "Enter sender email address: " sender

# Prompt for the email subject.
read -p "Enter email subject: " subject

# Prompt for the email body.
echo "Enter email body (end with an empty line): "
body=""
while IFS= read -r line; do
    [ -z "$line" ] && break
    body="$body$line\n"
done

# Prompt to send only the body or both body and a file.
read -p "Do you want to send the body only or both body and a file? (Enter 'body' or 'both'): " send_option

if [ "$send_option" == "both" ]; then
    # Prompt for the file name to attach.
    read -p "Enter file name to attach: " filename

    # Check if the file exists
    if [ -f "$filename" ]; then
        # Send the email with attachment
        echo -e "$body" | mail -s "$subject" -a "From: $sender" -A "$filename" "$recipient"
        echo "Email sent from $sender to $recipient with attachment $filename"
    else
        # File does not exist
        echo "File $filename does not exist. Email not sent."
    fi
else
    # Send the email without attachment
    echo -e "$body" | mail -s "$subject" -a "From: $sender" "$recipient"
    echo "Email sent from $sender to $recipient without attachment"
fi
