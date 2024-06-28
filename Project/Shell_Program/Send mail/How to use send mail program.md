# Email Sending Script Manual

This Bash script facilitates the sending of emails directly from the command line. It prompts the user for necessary information such as the recipient's email address, the sender's email address, the email subject, and the email body. After gathering this input, it composes the email and sends it using the `mail` command.

## How the Script Works

1. **Prompt for Recipient Email Address**: 
    - The script starts by asking the user to enter the recipient's email address and stores it in the variable `recipient`.

2. **Prompt for Sender Email Address**: 
    - Next, it asks for the sender's email address, storing it in the variable `sender`.

3. **Prompt for Email Subject**: 
    - The script then prompts the user to enter the subject of the email and saves it in the variable `subject`.

4. **Prompt for Email Body**: 
    - The script prompts the user to enter the body of the email. The user can type multiple lines, and the input ends when an empty line is entered. The body of the email is stored in the variable `body`.

5. **Send the Email**: 
    - The script sends the email using the `mail` command, with the email body piped to it. The `-s` flag specifies the subject, and the `-a` flag adds a "From" header to specify the sender's address.

6. **Confirmation Message**: 
    - After sending the email, the script prints a confirmation message indicating that the email was sent from the sender to the recipient.

## Script

```bash
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
```

### Usage Notes
Ensure that the mail command is installed and properly configured on your system.
The script assumes that the mail system on your machine can handle sending emails directly.
Proper authentication and configuration of the mail server might be required for sending emails successfully.
This script provides a simple and interactive way to send emails directly from the command line, making it a handy tool for various automation tasks.

