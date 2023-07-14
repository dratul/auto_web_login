# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
print("\n \n \n Do not close this window till you are working on this computer")
mybrowser = webdriver.Firefox()
WebDriverWait(mybrowser, 10)
mybrowser.get("http://172.16.40.5:8090/httpclient.html")
username = mybrowser.find_element("id","username") 
# Sending the keys for username     
username.send_keys("balkrishna")       
# Getting the password element                            
password = mybrowser.find_element("id", "password") 
    # Sending the keys for password   
password.send_keys("4")               
    # Getting the tag for submit button  
mybrowser.find_element("id", "loginbutton").click() 

# minimize window position
mybrowser.minimize_window()
#tell location of the webdriver and call it 'mybrowser'
mybrowser = webdriver.Firefox()
def new_func(mybrowser):
    mybrowser.get("http://172.16.40.5:8090/httpclient.html")

new_func(mybrowser)
WebDriverWait(mybrowser, 20)
# minimize window position
mybrowser.minimize_window()
while(True):
    mybrowser.close()
# Getting the login element
    mybrowser = webdriver.Firefox()
    WebDriverWait(mybrowser, 10)
    mybrowser.get("http://172.16.40.5:8090/httpclient.html")
    username = mybrowser.find_element("id","username") 
# Sending the keys for username     
    username.send_keys("balkrishna")       
# Getting the password element                            
    password = mybrowser.find_element("id", "password") 
    # Sending the keys for password   
    password.send_keys("4")               
    # Getting the tag for submit button  
    mybrowser.find_element("id", "loginbutton").click() 
#Time of 5 minute . this program is in while loop of 5 minutes
     # Minimize the window
# minimize window position
    mybrowser.minimize_window()
    time.sleep(300)