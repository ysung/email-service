import mandrill

class EmailServiceMandrill:
	'''
	This is the email sender class using the MailGun implementation. 
	With the api provided by Mandrill, the interface be implemented as 
	send(self, from_email, to_email, subject, text, cc_email, bcc_email)

	https://mandrillapp.com/api/docs/messages.JSON.html
	'''
	def __init__(self):
		# configuration file of the email sender implementation 
		self.mandrill_key = "27ZpDc-XlF0bkiaWhIYqBQ"
		self.mandrill_api_url = "https://mandrillapp.com/api/1.0/users/send.json"

	def send(self, from_email, to_email, subject = '', text = '', cc_email = [], bcc_email = []):
		'''
		to_email can be either one email or a list of mails.
		cc_email and bcc_email can be empty, one email, or a list of mails.

		return 0 if access, 1 if fail. 
		'''
		mandrill_client = mandrill.Mandrill(self.mandrill_key)
		message = {
		'from_email': from_email,
		'to':[],
		'test': text,
		'subject': subject
		}

		if len(to_email) > 0:
			if type(to_email) == str:
				to_email = [to_email]
			for item in to_email:
				message['to'] += [{'email': item, 'type': 'to'}]


		if len(cc_email) > 0:
			if type(cc_email) == str:
				cc_email = [cc_email]
			for item in cc_email:
				message['to'] += [{'email': item, 'type': 'cc'}]
		
		if len(bcc_email) > 0:
			if type(bcc_email) == str:
				bcc_email = [bcc_email]
			for item in bcc_email:
				message['to'] += [{'email': item, 'type': 'bcc'}]  

		result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool')
		status = 0 if result[0]['status'] == 'sent' else 1
		#print (result[0]['status'])
		return status

