# -*- coding:utf-8 -*-
"""Operations with files."""

import json
import os
import sys
from json.decoder import JSONDecodeError

import yaml
from yaml.scanner import ScannerError

EXT_ERROR_MSG = '\n{0} - invalid file extension\nuse one of: .json .yaml .yml'
YAML_ERROR_MSG = '\n{0} - incorrect YAML file'
JSON_ERROR_MSG = '\n{0} - incorrect JSON file'


def collect_data(file_path):
    _, ext = os.path.splitext(file_path)
    loader = {
        '.json': json.load,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load,
    }.get(ext.lower())
    sys.tracebacklimit = 0
    if not loader:
        raise RuntimeError(EXT_ERROR_MSG.format(file_path))
    try:
        with open(file_path) as data_file:
            return loader(data_file)
    except ScannerError as exc:
        raise RuntimeError(YAML_ERROR_MSG.format(file_path)) from exc
    except JSONDecodeError as exc:
        raise RuntimeError(JSON_ERROR_MSG.format(file_path)) from exc
