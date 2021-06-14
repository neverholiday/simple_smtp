#!/usr/bin/env python3
import os
import smtplib, ssl
import getpass

##########################################################
#
#	NOTE : Learn from https://realpython.com/python-send-email/
#

#	smptp host and port
smtpServer = "smtp.gmail.com"
port = 587  # For starttls

print( '###########################################################################' )
print( 'THIS IS TEST SCRIPT THAT ONLY SUPPORT GOOGLE MAIL PROVIDER (GMAIL).' )
print( '###########################################################################\n' )

#	sender and reciever email
senderEmail = input( 'Sender E-Mail : ' )
recieverEmail = input( 'Reciever E-Mail : ' )

#	reciever email
password = getpass.getpass('Sender E-Mail password : ')

message = """\
Subject: Hi there

This message is sent from Python script."""

# Create a secure SSL context
context = ssl.create_default_context()

# Use context, with statement to open server
with smtplib.SMTP( smtpServer, port ) as server:
	
	server.ehlo() # Can be omitted
	server.starttls( context=context ) # Secure the connection
	server.ehlo() # Can be omitted

	#	Login to mail server
	server.login( senderEmail, password )

	print( f'Send mail to {recieverEmail}...' )

	#	Send e-mail
	server.sendmail( senderEmail, recieverEmail, message )
	
	print( 'Done.' )