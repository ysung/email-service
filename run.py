from emailservice import EmailService
'''
This is the interface of test email service API.
Please provide valid from_email, to_email, cc_email, bcc_email, subject and text.
to_email can be either one email or a list of mails.
cc_email and bcc_email can be empty, one email, or a list of mails.
subject and text can not be both empty.
'''

if __name__ == "__main__":
	from_email = "from@mail.com"
	to_email = "to@mail.com"
	cc_email = ["cc1@mail.com", "cc2@mail.com"]
	bcc_email = ""
	subject = "Test Subject"
	text = "Test is a test text."

	result = EmailService.sentMail(from_email, to_email, subject, text)
	print (result)

