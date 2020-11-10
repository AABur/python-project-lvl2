# -*- coding:utf-8 -*-
"""Generating plain text output."""

import json


def generate_json_diff(diff):
    return json.dumps(diff)
