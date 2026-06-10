# Password Generator

A customizable password generator built in Python that creates secure random passwords based on user-defined criteria such as password length, numbers, uppercase letters, lowercase letters, and special characters.

## Features

* Generate passwords of any length
* Include or exclude:

  * Numbers
  * Uppercase letters
  * Lowercase letters
  * Special characters
* Input validation for password length
* User-friendly command-line interface
* Random password generation
* Lightweight and easy to use

---

## How It Works

The program first asks the user for the desired password length and validates the input to ensure it is a valid number.

Next, the user can choose which character categories should be included in the password:

* Numbers (0-9)
* Uppercase letters (A-Z)
* Lowercase letters (a-z)
* Special characters (!, @, #, $, etc.)

Based on the user's selections, the program creates a pool of allowed characters and randomly selects characters from that pool until the desired password length is reached.

---

## Requirements

* Python 3.x

No third-party libraries are required.

The project uses only Python's built-in modules:

```python
import random
import string
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/mratharvtrivedi/password-generator.git
```

Navigate to the project directory:

```bash
cd password-generator
```

Run the program:

```bash
python password_generator.py
```

---

## Usage

Example:

```text
Enter the length of password: 12

Do you want to include numbers ? (y/n): y
Do you want to include capital letters ? (y/n): y
Do you want to include small letters ? (y/n): y
Do you want to include special characters ? (y/n): y
```

Output:

```text
Generated Password: A7@kP2!mQ9#x
```

---

## Example Scenarios

### Numeric Password

Input:

```text
Length: 8
Numbers: y
Capital Letters: n
Small Letters: n
Special Characters: n
```

Output:

```text
49280173
```

---

### Alphanumeric Password

Input:

```text
Length: 10
Numbers: y
Capital Letters: y
Small Letters: y
Special Characters: n
```

Output:

```text
A9k2P7mQ1z
```

---

### Complex Password

Input:

```text
Length: 16
Numbers: y
Capital Letters: y
Small Letters: y
Special Characters: y
```

Output:

```text
A$8mQ!2z#P7@kL5x
```

---

## Project Structure

```text
password-generator/
│
├── password_generator.py
├── README.md
```

---

## Concepts Used

This project demonstrates several important Python concepts:

### Input Validation

```python
try:
    length = int(input())
except ValueError:
```

Used to ensure the user enters a valid number.

---

### Loops

```python
for _ in range(length):
```

Used to generate characters repeatedly until the desired password length is reached.

---

### Conditional Statements

```python
if num_c == "y":
```

Used to determine which character categories should be included.

---

### String Manipulation

Character pools are combined into a single string from which random characters are selected.

---

### Randomization

```python
random.choice()
```

Used to randomly select characters from the available character pool.

---

## Limitations

Current limitations:

* Does not guarantee at least one character from every selected category
* Uses the `random` module instead of the more secure `secrets` module
* Command-line interface only
* No password strength meter

---

## Future Improvements

Potential future enhancements:

* Use Python's `secrets` module for cryptographically secure password generation
* Add password strength analysis
* Create a graphical user interface (GUI)
* Export generated passwords to a file
* Copy passwords directly to clipboard
* Guarantee at least one character from each selected category

---

## Learning Objectives

This project was created to practice:

* Python fundamentals
* Exception handling
* Loops
* Conditional statements
* String manipulation
* Random number generation
* User input validation

---

## Disclaimer

This project is intended for educational and learning purposes. Generated passwords should be reviewed before use in production environments. For highly sensitive applications, consider using cryptographically secure password generation methods such as Python's `secrets` module.
