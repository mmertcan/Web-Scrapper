import pandas as pd
import numpy as np
import selenium
from selenium import webdriver
import os
import time
import smtplib
from email.message import EmailMessage



def web_scraper():


	driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver")) #works

	url = 'https://egov.uscis.gov/casestatus/landing.do'
	driver.get(url)

	# Find the textbox
	text_box = driver.find_element_by_id('receipt_number')

	text_box.click()

	#Define the keys
	my_case_num = 'MSC1990616973'
	check_status_box_name = 'initCaseSearch'


	#Send the case info
	text_box.send_keys(my_case_num)


	#Initiate on the 'Check Status' box
	check_status_button = driver.find_element_by_name(check_status_box_name)


	#Click on the 'Check Status' box
	check_status_button.click()


	info = driver.find_element_by_tag_name('p').text

	return info



def send_mail(message,email_subject,email_to):
	""" This function sends an email to preferred email address 
	Takes message, and email address as arguments"""

	#Get the email password and user from the local environment
	email_address = os.environ.get('EMAIL_USER')
	email_pass = os.environ.get('EMAIL_PASS')

	print(email_address)

	#Creating a message object
	msg = EmailMessage() 
	msg['Subject'] = email_subject
	msg['From'] = email_address
	msg['To'] = email_to
	msg.set_content(message)
	#Adding the gmail email server(creating smtp server with Google)
	with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:  
    
		smtp.login(email_address,email_pass)
    
    
		smtp.send_message(msg) 
	


to_email_address = 'mertmcan@gmail.com'
email_subject = 'Your case status result for today'

web_scraper()

time.sleep(5)

send_mail(web_scraper(),email_subject,to_email_address)