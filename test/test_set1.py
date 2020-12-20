import unittest
import pytest
import numpy as np
import pandas as pd
from numpy.testing import assert_almost_equal, assert_equal, assert_string_equal, assert_array_equal
from numpy.testing import assert_allclose, assert_raises, assert_raises_regex
import os
import sys
dir = os.path.dirname(os.path.abspath(__file__)) + '/'
data_dir = dir + '../data/'
lib_dir = dir + '..'
sys.path.append(lib_dir)
from lib.recommender_data import RECCOMEND_DATA
from lib.recommender_tools import get_ouput, group_by_kpi
from app import get_engine_output, get_feature_output



rec_data = RECCOMEND_DATA()
def test_basic_test():
    out = {}
    assert_equal(isinstance(out, dict), True)


def test_engine_output():
    """test get engine output api result to know if it return the right type of data that was expected"""
    result = get_engine_output()
    message =f'Should return output tuple but returned {type(result)}'
    assert isinstance(result, tuple),  message

def test_update_data():
    """test if update data is getting data and converting it to dictionary"""
    x = rec_data.update_data()
    assert isinstance(x, dict), "update data didn't return data"

def test_extract_game_features():
    """test if recommed data update function returns a dictionary this query was used in app.py file"""
    game_id = "f910338e60315f02812b05e932068f47"
    ret = rec_data.extract_game_features(game_id=game_id)    
    assert isinstance(ret, dict), "extract_game_features did not return values"

def test_feature_output():
    """Test if feature output is returning the required result"""
    result = get_feature_output()
    assert isinstance(result, tuple), f"feature_output has an error it return {result}"
