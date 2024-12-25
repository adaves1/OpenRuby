# Coding Standards

## 1. Introduction
This document outlines the coding standards for the OpenRuby project to ensure consistency, readability, and maintainability across all codebases. Following these guidelines will help streamline collaboration and reduce bugs.

## 2. General Guidelines
- **Code must be readable** – Write code as if the next person to maintain it is a beginner.
- **Consistency is key** – Follow the same style throughout the codebase.
- **Minimal comments, maximum clarity** – Use clear and descriptive code. Comment only when necessary.

---

## 3. Formatting

### 3.01 Python Enhancement Proposal Guidelines
Follow the PEP8 (Python Enhancement Proposal 0008) Guidelines at [Python.org](https://peps.python.org/pep-0008/) to format your code or read the paragraphs given below.

### 3.1 Indentation
- Use **4 spaces** per indentation level (no tabs).
- Continuation lines should align with the opening delimiter.

### 3.2 Line Length
- Limit all lines to a maximum of **80 characters**.
- Break long statements into multiple lines.

### 3.3 Brackets
- Use **K&R style** for braces:
  ```python
  def example():
      if condition:
          statement
  ```

### 3.4 Whitespace
- Use a single blank line between functions and classes.
- Avoid trailing whitespace.

---

## 4. Naming Conventions

### 4.1 Variables and Functions
- Use **snake_case** for variable and function names.
  ```python
  def process_data(input_value):
      return input_value * 2
  ```

### 4.2 Classes
- Use **PascalCase** for class names.
  ```python
  class DataProcessor:
      pass
  ```

### 4.3 Constants
- Use **ALL_CAPS** for constants.
  ```python
  MAX_RETRIES = 5
  ```

---

## 5. Error Handling
- Always handle exceptions and errors explicitly.
- Avoid silent failures.
  ```python
  try:
      result = perform_task()
  except ValueError as e:
      print(f"Error: {e}")
  ```

---

## 6. Documentation
- Use docstrings for all public classes and functions.
  ```python
  def add_numbers(a, b):
      """
      Adds two numbers together.

      Args:
          a (int): First number.
          b (int): Second number.

      Returns:
          int: Sum of the two numbers.
      """
      return a + b
  ```

---

## 7. Testing
- Write unit tests for all critical functions.
- Use automated testing frameworks like `pytest` or `unittest`.

---

## 8. Version Control
- Use clear and concise commit messages.
- Group related changes into a single commit.

---
