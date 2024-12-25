# OpenRuby

**Version:** 1.02.0
**Authors:** Anthony Daves and  John Daves

---

## Overview
`OpenRuby` is a Python package designed to provide robust functionality for performing various types of complex or simple math and string operations. It is built to be modular and extensible, allowing developers to easily integrate it into their existing projects or use it as a foundation for new ones.

The module consists of multiple submodules, each handling a distinct part of the overall functionality. This ensures a clean separation of concerns and allows for greater maintainability and scalability.

---

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Module Structure](#module-structure)
- [Configuration](#configuration)
- [Examples](#examples)
- [Advanced Features](#advanced-features)
- [Error Handling](#error-handling)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

---

## Installation
To install `OpenRuby`, clone the repository and include the module in your project directory.

```bash
git clone https://github.com/adaves1/OpenRuby-Library.git

cd openruby
```
Alternatively, you can install the module by adding it to your Python path:

```python
import sys
sys.path.append('/path/to/openruby')
```

Ensure that Python 3.6 or higher is installed, as `openruby` leverages modern Python features.

---

## Usage
Once installed, import the module and initialize it to ensure proper configuration loading.

```python
import openruby
openruby.initialize()
```

You can now access key functions and classes from the submodules:

```python
from openruby import ActionFlow, version
obj = Actionflow("af", 41, 00)
result = version()
```

---

## Module Structure
The `openruby` package is structured for clarity and extensibility:

```
openruby/
│
├── __init__.py       
├── Algorithms.py
├── Base.py 
├── BasicMath.py
├── Bitwise.py
├── ComplexMath.py
├── config.json
├── Constants.py
├── Converters.py
├── GeometricAnimations.py
├── OpenRuby.py
├── Random.py
├── Solvers.py
├── String.py
└── Trigonometry.py
     
```
- **`__init__.py`**: Handles module initialization and configuration loading.
- **`Algorithms.py`**: Implements various algorithms and N-Grams implementation.
- **`Base.py`**: Implements conversion of bases.
- **`BasicMath.py`**: Implements various basic math operations.
- **`Bitwise.py`**: Implements bitwise operations.
- **`ComplexMath.py`**: Implements various complex math operations. 
- **`config.json`**: Stores metadata in the form of JSON.
- **`Constants.py`**: Implements various constants like PI and GOLDEN RATIO.
- **`Converters.py`**: Implements functions for converting units.
- **`GeometricAnimations.py`**: Implements functions to generate animation seeds that can be used as a animation seed generator or as a port in animations.
- **`OpenRuby.py`**: Implements functions to store actionflows.
- **`Random.py`**: Implements functions to generate random numbers in core Python.
- **`Solvers.py`**: Implements functions to solve games and problems such as Sudoku and Game of life.
- **`String.py`**: Implements functions for string operations.
- **`Trigonometry.py`**: Implements trigonometry formulae such as Secant and Archaeic Tangent.

The modular design makes it easy to expand the package by adding new submodules.

---

## Configuration
The module relies on a `config.json` file for initialization. Place this file in the root directory.

The configuration file allows fine-tuned control over module behavior, including logging and feature toggles.

---

## Examples
### Basic Example 1
```python
from openruby import Random, rand_range
obj = Random()
result = rand_range(10, 1, 10000)
print(result)
```

### Advanced Example 1
```python
import openruby
from openruby import Random

openruby.initialize()
obj = Random()
obj.generate_password(8)
```

### Configuration Example 1
```python
import openruby
settings = openruby.settings
print(settings)
```

---

## Advanced Features
- **Custom Logging**: Supports configurable logging levels and output formats.
- **Error Recovery**: Graceful handling of runtime errors with fallback mechanisms.
- **Parallel Processing**: Leverages multithreading to improve performance.

---

## Error Handling
`openruby` includes robust error handling to ensure stability. Errors are logged, and appropriate exceptions are raised with detailed messages.

---

## Testing
Unit tests are included to ensure all components function as expected.
Run tests using:

```bash
python -m unittest discover tests
```

### Test Structure
- **Unit Tests** – Located in the `tests/unit` directory, focusing on individual functions or classes.
- **Integration Tests** – Located in the `tests/integration` directory, testing interactions between components.
- **Config Testing** – Tests related to different configuration scenarios are under `tests/config`.

### Writing Tests
When writing new tests:
- Use the `unittest` module.
- Ensure test names follow the `test_` prefix (e.g., `test_dijkstra`).
- Place new tests in the relevant directory (`unit`, `integration`, or `config`).

Example:
```python
import unittest
from openruby import Trigonometry

class TestSine(unittest.TestCase):
    def test_valid_input(self):
        result = openruby.Trigonometry.(65))
        self.assertEqual(result, 0.9063)
```

---

## Contributing
Contributions are encouraged! Whether it’s bug fixes, new features, or documentation improvements, we welcome your input.

**How to contribute:**
1. Fork the repository.
2. Create a new feature branch.
3. Implement your changes and commit.
4. Submit a pull request.

---

## License
`OpenRuby` is licensed under the MIT License. Use, modify, and distribute it freely.

