# Password Generator

This is a simple Python program that generates a random password based on user input. The generated password will meet specific criteria:

- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character
- The total length of the password must be between **6** and **16 characters**.

## Features

- The user is prompted to select how many uppercase letters, lowercase letters, digits, and special characters they want in the password.
- The program ensures that the password meets the required criteria and length.
- The generated password is shuffled to ensure randomness.

## Requirements

- Python 3.x

## How to Use

1. Run the Python script.
2. The program will prompt you to enter how many uppercase characters, lowercase characters, digits, and special characters you would like in the password. The values must be between 1 and 13 for each category.
3. Once the criteria are valid (total length between 6 and 16 characters), the program will generate a password and display it.

### Example:

```plaintext
Password Generator
password must include: 
1 Upper Case
1 Lower Case
1 Digit 
1 Special Character
Minimum  Length is 6 total Characters
Maximum  Length is 16 total Characters

How many Uppercase Characters: 3
How many Lowercase Characters: 4
How many Digits: 2
How many Special Characters: 2

You have selected 11 characters
Your password is:   V7n3#$uYjW
