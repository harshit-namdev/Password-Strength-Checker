

---

# Password Strength Checker 🔒

A Python-based tool that checks the strength of a password based on length and character variety. If the entered password is weak, the tool suggests a stronger, randomly generated password. This is ideal for beginners in cybersecurity or Python programming who want to understand password security basics.

## Features
- **Password Strength Evaluation**: Checks for length, uppercase, lowercase, numbers, and special characters.
- **Strength Rating**: Provides feedback with one of three levels—"Weak," "Moderate," or "Strong."
- **Password Generator**: Suggests a secure, randomly generated password when a stronger option is needed.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/harshit-namdev/Password-Strength-Checker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Password-Strength-Checker
   ```

3. Make sure you have **Python 3.x** installed. You can check your version by running:
   ```bash
   python --version
   ```

## Usage
1. Run the script:
   ```bash
   python password_strength_checker.py
   ```

2. Enter a password when prompted to check its strength.
3. If the password is not strong, the program will suggest a randomly generated secure password.

## Example Output

```plaintext
Enter a password to check its strength: mypassword123
Password Strength: Weak

Consider using a stronger password. Here's a suggestion:
AJk2#8@zNl3*Qp
```

## How It Works
The script analyzes the following criteria to determine password strength:
- **Length**: Shorter passwords are inherently less secure.
- **Character Variety**: Checks for uppercase, lowercase, numbers, and special symbols.
- **Overall Score**: Combines the checks to classify the password as "Weak," "Moderate," or "Strong."

## Contributing
Contributions are welcome!

---
