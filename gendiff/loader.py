# -*- coding:utf-8 -*-
"""Operations with files."""

import json
import os
from json.decoder import JSONDecodeError

import yaml
from yaml.scanner import ScannerError


def collect_data(file_path):
    loaders = {
        '.json': json.load,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load,
    }
    call_loader = loaders.get
    correct_exts = loaders.keys()
    _, ext = os.path.splitext(file_path)
    if ext not in correct_exts:
        exit(''.join(('Incorrect file ', file_path)))
    try:
        with open(file_path) as data_file:
            return call_loader(ext)(data_file)
    except FileNotFoundError:
        exit(''.join(('File not found ', file_path)))
    except ScannerError:
        exit(''.join(('Wrong YAML file ', file_path)))
    except JSONDecodeError:
        exit(''.join(('Wrong JSON file ', file_path)))
