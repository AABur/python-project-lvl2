# -*- coding:utf-8 -*-
"""Generating plain text output."""

import json


def format_json(diff):
    return json.dumps(diff)
