# Gendiff

[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![Maintainability](https://api.codeclimate.com/v1/badges/819fe1aa42985a7b2dc5/maintainability)](https://codeclimate.com/github/AABur/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/819fe1aa42985a7b2dc5/test_coverage)](https://codeclimate.com/github/AABur/python-project-lvl2/test_coverage)
![CitHub_CI](https://github.com/AABur/python-project-lvl2/workflows/CH_CI/badge.svg)

## Script

```bash
$ gendiff -h
usage: gendiff [-h] [-f FORMAT] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```

## Function

```bash
from gendiff import generate_diff

diff = generate_diff(file_path1, file_path2)
print(diff)
```
