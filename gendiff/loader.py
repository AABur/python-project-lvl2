# -*- coding:utf-8 -*-
"""Operations with files."""

import json
import os
from json.decoder import JSONDecodeError

import yaml
from yaml.scanner import ScannerError

EXT_ERROR_MSG = '{0} - invalid file extension\nuse one of: .json .yaml .yml'
YAML_ERROR_MSG = '{0} - incorrect YAML file'
JSON_ERROR_MSG = '{0} - incorrect JSON file'
OS_ERROR_MSG = '{0} - file access error'


call_loader = {
    '.json': json.load,
    '.yaml': yaml.safe_load,
    '.yml': yaml.safe_load,
}.get


class GendiffError(Exception):
    pass  # noqa: WPS420, WPS604


# TODO error massage and traceback
def collect_data(file_path):
    _, ext = os.path.splitext(file_path)
    loader = call_loader(ext.lower())
    if not loader:
        raise GendiffError(EXT_ERROR_MSG.format(file_path))
    try:
        with open(file_path) as data_file:
            return loader(data_file)
    except ScannerError as err:
        raise GendiffError(err, YAML_ERROR_MSG.format(file_path))
    except JSONDecodeError as err:
        raise GendiffError(err, JSON_ERROR_MSG.format(file_path))
    except OSError as err:
        raise GendiffError(err, OS_ERROR_MSG.format(file_path))
