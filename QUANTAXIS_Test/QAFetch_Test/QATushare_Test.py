# -*- coding:utf-8 -*-
"""
Created on 2019/7/27 17:00
@author: Leo
@file:QATushare_Test.py
@desc:
"""
import unittest
import QUANTAXIS as qa


class Test_QA_Fetch(unittest.TestCase):
    def test_QA_fetch_get_stock_realtime(self):
        df1=qa.QA_fetch_get_stock_realtime('tdx','000001')
        df2=qa.QA_fetch_get_stock_realtime('tdx','161728')
        print(df2)
        self.assertEqual(len(df1),1)
        self.assertEqual(len(df2),1)