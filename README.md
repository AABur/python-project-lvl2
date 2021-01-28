# Gendiff

![Actions Status](https://github.com/AABur/python-project-lvl2/workflows/hexlet-check/badge.svg)
![CitHub_CI](https://github.com/AABur/python-project-lvl2/workflows/CitHub_CI/badge.svg)
![CodeQL](https://github.com/AABur/python-project-lvl2/workflows/CodeQL/badge.svg)

[![Maintainability](https://api.codeclimate.com/v1/badges/819fe1aa42985a7b2dc5/maintainability)](https://codeclimate.com/github/AABur/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/819fe1aa42985a7b2dc5/test_coverage)](https://codeclimate.com/github/AABur/python-project-lvl2/test_coverage)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

[![Challenge | 100 Days of Code](https://img.shields.io/static/v1?label=Challenge&labelColor=384357&message=100%20Days%20of%20Code&color=00b4ee&style=for-the-badge&link=https://www.100daysofcode.com)](https://www.100daysofcode.com)

Gendiff (GENerator of DIFFerences) - a program defining the difference between two data structures (JSON or YAML) and generating new structure containing differences details (including unchanged).

## Features

- Supported input formats: YAML, JSON
- Report generation as plain text, structured text and JSON
- Usage as CLI util or library function

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install gendiff.

```bash
pip install --user --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ AABur_gendiff
```

Installation and usage example

[![asciicast](https://asciinema.org/a/RfBQHFrCASCMU23WeeAeSKA0J.svg)](https://asciinema.org/a/RfBQHFrCASCMU23WeeAeSKA0J)

## Usage

### As library function

```python
from gendiff import generate_diff

diff = generate_diff(file_path1, file_path2, style)
print(diff)
```

### As CLI util

```bash
❯ gendiff -h
usage: gendiff [-h] [-f FORMAT] first_file second_file

Generate difference of two JSON or YAML files.

positional arguments:
  first_file            first file to compare
  second_file           second file to compare

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set output format ['json', 'plain', 'stylish']
                        (default: 'stylish')
```

### Usage examples

#### JSON output (-f json)

[![asciicast](https://asciinema.org/a/sdpmQxH2aMUQwKmCCIUl49gzn.svg)](https://asciinema.org/a/sdpmQxH2aMUQwKmCCIUl49gzn)

#### Structured output (-f stylish)

[![asciicast](https://asciinema.org/a/W1Xb1yNhEbYBLZSYHIa8ALhkV.svg)](https://asciinema.org/a/W1Xb1yNhEbYBLZSYHIa8ALhkV)

#### Plain output (-f plain)

[![asciicast](https://asciinema.org/a/0tXY4DIYfArT1hu56Wo6Gwq0u.svg)](https://asciinema.org/a/0tXY4DIYfArT1hu56Wo6Gwq0u)

## Contributing

This is a learning project and the contribution is not accepted.

## License

[MIT License](https://github.com/AABur/python-project-lvl2/blob/master/LICENSE)
