# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 18:16:23 2018

@author: nnair
"""

from ..build import q01_missing_words
from unittest import TestCase
from inspect import getfullargspec

s='I want two apples and two oranges'
t='I want two green apples'

common=q01_missing_words(s,t)
c_list=['and', 'two', 'oranges']

class TestRead_csv_data_to_df(TestCase):
    def test_argument_size(self):
        arg = getfullargspec(q01_missing_words).args
        self.assertEqual(len(arg), 2, "Expected argument(s) %d, Given %d" % (2, len(arg)))

    def test_return_instance(self):
        self.assertIsInstance(common, list,
                              "The Expected return type does not match with the given return type")

    def test_common_list(self):
        self.assertListEqual(sorted(common), sorted(c_list), "The missing elements not found properly ")    
    
    