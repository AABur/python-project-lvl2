# -*- coding:utf-8 -*-
"""Generate diff tests."""

import pytest

from gendiff.formaters.formater import GendiffFormaterError, call_formater


def test_wring_style_formater():
    with pytest.raises(GendiffFormaterError):
        assert call_formater({}, 'wromg_style')
