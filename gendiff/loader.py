# -*- coding:utf-8 -*-
"""Operations with files."""

import json
import os
from json.decoder import JSONDecodeError

import yaml
from yaml.scanner import ScannerError


class FileError(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        if self.message:
            return '{0} '.format(self.message)
        return 'MyCustomError has been raised'


def collect_data(file_path):
    _, ext = os.path.splitext(file_path)
    loader = {
        '.json': json.load,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load,
    }.get(ext.lower())
    if not loader:
        raise FileError(''.join(('Not correct JSON/YAML file ', file_path)))
    try:
        with open(file_path) as data_file:
            return loader(data_file)
    except (ScannerError, JSONDecodeError):
        raise FileError(''.join(('Not correct JSON/YAML file ', file_path)))
    except OSError as error:
        raise FileError(''.join((error.args[1], ' ', file_path)))
