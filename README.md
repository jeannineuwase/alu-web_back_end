# ALU Web Back End

## Project Overview

This project contains exercises focused on Python variable annotations, a key feature introduced in Python 3.5. Variable annotations help in improving code clarity, enabling better static type checking, and providing insights into the expected types of variables, function parameters, and return values.

## Exercises

### 1. `1-concat.py`

- **Function**: `concat`
- **Description**: Concatenates two strings.
- **Type Annotations**:
  - `str1: str`
  - `str2: str`
  - `return: str`

### 2. `2-floor.py`

- **Function**: `floor`
- **Description**: Returns the floor of a float.
- **Type Annotations**:
  - `n: float`
  - `return: int`

### 3. `3-to_str.py`

- **Function**: `to_str`
- **Description**: Converts a float to its string representation.
- **Type Annotations**:
  - `n: float`
  - `return: str`

### 4. `4-define_variables.py`

- **Description**: Defines and annotates several variables:
  - `a: int = 1`
  - `pi: float = 3.14`
  - `i_understand_annotations: bool = True`
  - `school: str = "Holberton"`

### 5. `5-sum_list.py`

- **Function**: `sum_list`
- **Description**: Calculates the sum of a list of floats.
- **Type Annotations**:
  - `input_list: List[float]`
  - `return: float`

### 6. `6-sum_mixed_list.py`

- **Function**: `sum_mixed_list`
- **Description**: Calculates the sum of a list containing both integers and floats.
- **Type Annotations**:
  - `mxd_lst: List[Union[int, float]]`
  - `return: float`

### 7. `7-to_kv.py`

- **Function**: `to_kv`
- **Description**: Converts a string and a number to a tuple, where the number is squared.
- **Type Annotations**:
  - `k: str`
  - `v: Union[int, float]`
  - `return: Tuple[str, float]`

### 8. `8-make_multiplier.py`

- **Function**: `make_multiplier`
- **Description**: Returns a function that multiplies a float by a given multiplier.
- **Type Annotations**:
  - `multiplier: float`
  - `return: Callable[[float], float]`

### 9. `9-element_length.py`

- **Function**: `element_length`
- **Description**: Returns a list of tuples containing elements and their lengths.
- **Type Annotations**:
  - `lst: Iterable[Sequence]`
  - `return: List[Tuple[Sequence, int]]`

## How to Run

Each Python file can be run individually to test the corresponding function. For example:

```bash
python3 1-main.py
```
