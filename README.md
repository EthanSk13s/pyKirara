[![Documentation Status](https://readthedocs.org/projects/pykirara/badge/?version=latest)](https://pykirara.readthedocs.io/en/latest/?badge=latest)
# pyKirara

pyKirara is a Python library for the starlight.kirara REST API

[Basic Documentation](https://pykirara.readthedocs.io/en/latest/)

## Usage

```python
import pyKirara

uzuki = pyKirara.Idol(101)

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
[MIT](https://choosealicense.com/licenses/mit/)
