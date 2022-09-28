import unittest
from selenium import webdriver
import time

edge = webdriver.Edge(r"C:\Users\HARI\OneDrive\Desktop\msedgedriver.exe")
edge.get('https://www.gmail.com')
print('title',edge.title)
edge.get('https://www.facebook.com')
edge.back()
edge.forward()
edge.close()



        