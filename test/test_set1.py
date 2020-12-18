import unittest
import numpy as np
from numpy.testing import assert_almost_equal, assert_equal, assert_string_equal
from numpy.testing import assert_allclose, assert_raises, assert_raises_regex
from lib.recommender_data import RECCOMEND_DATA
from lib.recommender_tools import get_ouput

rec_data = RECCOMEND_DATA()
def test_basic_test():
    out = {}
    assert_equal(isinstance(out, dict), True)
    

def test_extract_game():
    assert extract_game_features()