from emailservicemailgun import EmailServiceMailGun
from emailservicemandrill import EmailServiceMandrill

class EmailService:
	'''
	This class is the send-mail service interface.
	A service that accepts the necessary information and sends emails. 
	It should provide an abstraction between two different email service providers. 
	If one of the services goes down, your service can quickly failover to a 
	different provider without affecting your customers.

	status message  
	0      success
	1      from email address invalid
	2      to mail addreaa in vaild
	3      subject and text both are empty
	4      both two email sender failed in sending

	'''
	def sentMail(from_email, to_email, subject = '', text = '', cc_email = [], bcc_email = []):
		senders = []
		senders.extend([EmailServiceMailGun(), EmailServiceMandrill()])
		id = 0
		message = ''

		if from_email is None or len(from_email) == 0:
			return 1, 'Please provide valid from email address.'
		if to_email is None or len(to_email) == 0:
			return 2, 'Please provide at least one valid to email address.'
		if not subject and not text:
			return 3, 'subject and text both are empty'

		status = senders[id].send(from_email, to_email, subject, text, cc_email, bcc_email)

		if status == 0:
			message = 'success'
		else:
		#failover to another email service provider implementation
			id = (id + 1) % len(senders)
			status = senders[id].send(from_email, to_email, subject, text, cc_email, bcc_email)

		if status == 0:
			message = 'success'
		else:
			status = 4
			message = 'Emails failed in sending'

		return status, message



