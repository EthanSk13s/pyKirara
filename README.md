# pyKirara

pyKirara is a Python library for the starlight.kirara REST API

## Usage

```python
import pykirara

uzuki = pykirara.Idol(101)

print(f"HI! MY NAME IS {uzuki.conventional}")
print("I'll do my best!")
print(f"I'am {uzuki.age} years old!")

# Returns:
# HI! MY NAME IS Shimamura Uzuki
# I'll do my best!
# I'am 17 years old!
```

## Requirements
- Python 3.6 (Will make backwards compatible)
- [Requests](https://github.com/kennethreitz/requests) library

## License
[GPL](https://choosealicense.com/licenses/gpl-3.0/)