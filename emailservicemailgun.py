import requests

class EmailServiceMailGun:
	'''
	This is the email sender class using the MailGun implementation. 
	With the api provided by MailGun, the interface be implemented as 
	send(self, from_email, to_email, subject, text, cc_email, bcc_email)

	http://documentation.mailgun.com/user_manual.html#sending-via-api
	'''
	def __init__(self):
		# configuration file of the email sender implementation 
		self.mailgun_key = "key-09270647a871aa0b1ce2d05988017414"
		self.mailgun_api_url = "https://api.mailgun.net/v2/sandbox98ccd8ddccb641988f6e04bde006e722.mailgun.org/messages"

	def send(self, from_email, to_email, subject = '', text = '', cc_email = [], bcc_email = []):
		'''
		to_email can be either one email or a list of mails.
		cc_email and bcc_email can be empty, one email, or a list of mails.

		return 0 if access, 1 if fail. 
		'''
		message = {"from": from_email, 
		"to": to_email, 
		"subject": subject, 
		"text": text, 
		"cc": cc_email, 
		"bcc": bcc_email
		}
		if len(cc_email) == 0:
			message["cc"] = []
		if len(bcc_email) == 0:
			message["bcc"] = []

		result = requests.post( 
			self.mailgun_api_url,
			auth = ("api", self.mailgun_key),
			data = message
		)
		
		status = 0 if result.status_code == 200 else 1
		#print (result.status_code)
		return status

