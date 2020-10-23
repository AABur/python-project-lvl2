# Gendiff

Gendiff (GENerator of DIFFerences) - a program defining the difference between two data structures (JSON or YAML) and generating new structure containing differences details (including unchanged).

[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![Maintainability](https://api.codeclimate.com/v1/badges/819fe1aa42985a7b2dc5/maintainability)](https://codeclimate.com/github/AABur/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/819fe1aa42985a7b2dc5/test_coverage)](https://codeclimate.com/github/AABur/python-project-lvl2/test_coverage)
![CitHub_CI](https://github.com/AABur/python-project-lvl2/workflows/CitHub_CI/badge.svg)

## Features

- Supported input formats: YAML, JSON
- Report generation as plain text, structured text and JSON
- CLI util - `gendiff first_file second_file`
- library function - `from gendiff import generate_diff`

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

diff = generate_diff(file_path1, file_path2)
print(diff)
```

### As CLI util

```bash
❯ gendiff -h
usage: gendiff [-h] [-f {structured,plain,json}] first_file second_file

Generate difference of two JSON or YAML files.

positional arguments:
  first_file            first file to compare
  second_file           second file to compare

optional arguments:
  -h, --help            show this help message and exit
  -f {structured,plain,json}, --format {structured,plain,json}
                        set output format (default: structured)
```

### Usage examples

#### JSON output

[![asciicast](https://asciinema.org/a/sdpmQxH2aMUQwKmCCIUl49gzn.svg)](https://asciinema.org/a/sdpmQxH2aMUQwKmCCIUl49gzn)

#### Structured output

[![asciicast](https://asciinema.org/a/W1Xb1yNhEbYBLZSYHIa8ALhkV.svg)](https://asciinema.org/a/W1Xb1yNhEbYBLZSYHIa8ALhkV)

#### Plain output

[![asciicast](https://asciinema.org/a/0tXY4DIYfArT1hu56Wo6Gwq0u.svg)](https://asciinema.org/a/0tXY4DIYfArT1hu56Wo6Gwq0u)

## License

[MIT](https://choosealicense.com/licenses/mit/)
