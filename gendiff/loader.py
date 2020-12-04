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
OS_ERROR_MSG = '\n{0} - file access error'


class GendiffError(Exception):
    pass


# TODO error massage and traceback
def collect_data(file_path):
    _, ext = os.path.splitext(file_path)
    loader = _call_loader(ext)
    sys.tracebacklimit = 0
    if not loader:
        raise RuntimeError(EXT_ERROR_MSG.format(file_path))
    try:
        with open(file_path) as data_file:
            return loader(data_file)
    except ScannerError:
        raise GendiffError(YAML_ERROR_MSG.format(file_path))
    except JSONDecodeError:
        raise GendiffError(JSON_ERROR_MSG.format(file_path))
    except OSError:
        raise GendiffError(OS_ERROR_MSG.format(file_path))


def _call_loader(ext):
    return {
        '.json': json.load,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load,
    }.get(ext.lower())
