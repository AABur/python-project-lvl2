# -*- coding:utf-8 -*-

import pytest

from gendiff.formaters.formater import GendiffFormaterError, call_formater


def test_wrong_style_formater():
    with pytest.raises(GendiffFormaterError):
        assert call_formater({}, 'wrong_style')
