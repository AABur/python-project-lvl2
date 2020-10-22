# -*- coding:utf-8 -*-
"""Operations with files."""

import json
import os
from json.decoder import JSONDecodeError

import yaml
from yaml.scanner import ScannerError


class WrongFileError(Exception):
    """Special exception for wrong files."""

    def __init__(self, file_path):
        """Exception WrongFileError init.

        Args:
            file_path (str): file path
        """
        self.file_path = file_path

    def __str__(self):
        """Meaasage for WrongFileError.

        Returns:
            (str): error message
        """
        return 'Wrong file {0}'.format(self.file_path)


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
        raise WrongFileError(file_path)
    try:
        with open(file_path) as data_file:
            return call_loader(ext)(data_file)
    except (FileNotFoundError, ScannerError, JSONDecodeError):
        raise WrongFileError(file_path)
