# -*- coding:utf-8 -*-

import json
import os
from json.decoder import JSONDecodeError

import yaml
from yaml.scanner import ScannerError

EXT_ERROR_MSG = '{0} - invalid file extension\nuse one of: .json .yaml .yml'
YAML_ERROR_MSG = '{0} - incorrect YAML file'
JSON_ERROR_MSG = '{0} - incorrect JSON file'
OS_ERROR_MSG = '{0} - file access error'


class GendiffFileError(Exception):
    pass  # noqa: WPS420, WPS604


get_loader = {
    '.json': json.load,
    '.yaml': yaml.safe_load,
    '.yml': yaml.safe_load,
}.get


def collect_data(file_path):
    _, ext = os.path.splitext(file_path)
    call_loader = get_loader(ext.lower())
    if not call_loader:
        raise GendiffFileError(EXT_ERROR_MSG.format(file_path))
    try:
        with open(file_path) as data_file:
            return call_loader(data_file)
    except ScannerError:
        raise GendiffFileError(YAML_ERROR_MSG.format(file_path))
    except JSONDecodeError:
        raise GendiffFileError(JSON_ERROR_MSG.format(file_path))
    except OSError:
        raise GendiffFileError(OS_ERROR_MSG.format(file_path))
