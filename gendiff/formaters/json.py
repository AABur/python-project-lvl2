# -*- coding:utf-8 -*-
"""Generating plain text output."""

import json


def prepare_json(diff):
    return json.dumps(diff)
