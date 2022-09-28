
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium import webdriver
import time




class automating(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        global edge_auto
        edge_auto = webdriver.Edge(r"C:\Users\HARI\OneDrive\Desktop\msedgedriver.exe")
        edge_auto.get('https://www.google.com')
    def test_edge(self):
        edge_auto.find_element_by_name('q').send_keys('fitgirl repack')
        time.sleep(5)
        edge_auto.find_element_by_name('btnK').click()
        time.sleep(5)
        edge_auto.find_element(By.LINK_TEXT,'HMS').click()
        time.sleep(10)
    @classmethod
    def tearDownClass(self):
        edge_auto.close()
unittest.main()
