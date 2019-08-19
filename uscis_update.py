import pandas as pd
import numpy as np
import selenium
from selenium import webdriver
import os
import time
import smtplib
from email.message import EmailMessage


# #Initiate the driver
# driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver")) #works

# #Url to pull the data from
# url = 'https://egov.uscis.gov/processing-times/'

# driver.get(url)

# # Find the Form box
# form_clickable = driver.find_element_by_class_name('form-control')

# #Assign the variables
# key= "I-765 | Application for Employement Authorization"
# office_key = 'National Benefits Center'
# field_id_name = 'officeOrCenter'

# ## Click on the forms
# form_clickable.click()

# ## Click on the EAD form
# form_clickable.send_keys(key)


# # find the processing time tab in the form
# processing_time = driver.find_element_by_partial_link_text('Get processing time')

# # Find the Field Office or Service Center box
# form_field = driver.find_element_by_id(field_id_name)

# #Click on the form
# form_field.click()

# #Add timer to remove conflict with two forms are interfering each other
# time.sleep(5)


# # Send the office key we want from the output of the click
# form_field.send_keys(office_key)


# # Click on the processing time form
# processing_time.click()

# time.sleep(5)

# ## Get last inquiry date
# date = driver.find_element_by_id('date')

# date = date.text ## Grab the information ab out the last inquiry date on USCIS website

# print(date)


date = 'March 03, 2019'


def send_mail():
	""" This function sends an email to my own email address """
	#Get the email password and user from the local environment
	email_address = os.environ.get('EMAIL_USER')
	email_pass = os.environ.get('EMAIL_PASS')

	print(email_address)


	msg = EmailMessage() #Creating a message object
	msg['Subject'] = 'Email test subject'
	msg['From'] = email_address
	msg['To'] = 'mertmcan@gmail.com'
	msg.set_content(date)

	with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:#Adding the gmailemailserver(creating smtp server with Google)
    
		smtp.login(email_address,email_pass)
    
    
		smtp.send_message(msg)  # Format: smtp.sendmail(SENDER, RECEIVER, message)



send_mail()










