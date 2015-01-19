from emailservicemailgun import EmailServiceMailGun
from emailservicemandrill import EmailServiceMandrill

def sentMail(fromEmail, toEmail, subject, text, ccEmail, bccEmail):
	senders = []
	senders.extend([EmailServiceMailGun(), EmailServiceMandrill()])
	id = 0
	message = ''

	if fromEmail is None or len(fromEmail) == 0:
		return 1, 'from email address invalid'
	if toEmail is None or len(toEmail) == 0:
		to_list = []
	if ccEmail is None or len(ccEmail) == 0:
		ccEmail = []
	if bccEmail is None or len(bccEmail) == 0:
		bccEmail = []
	if len(toEmail) == 0 and len(ccEmail) == 0 and len(bccEmail) == 0:
		return 2, 'No valid to/cc/bcc email address. Please provide at least one valid to/cc/bcc email address.'

	if not subject and not text:
		return 3, 'subject and text both are empty'
	elif not subject:
		suject = ''
	elif not text:
		text = ''

	status = senders[id].send(fromEmail, toEmail, subject, text, ccEmail, bccEmail);

	if status == 0:
		message = 'success'
	else:
	#failover to another email service provider implementation
		id = (id + 1) % len(senders)
		status = senders[id].send(fromEmail, toEmail, subject, text, ccEmail, bccEmail);
	if status == 0:
		message = 'success'
	else:
		status = 4
		message = 'Emails failed in sending. The error message is as followed:\n' + message

	return status, message



if __name__ == "__main__":
	_fromEmail = "s.yunchieh@gmail.com"
	_toEmail = ["ysung@ucdavis.edu","cuitjason@hotmail.com"]
	_ccEmail = ""
	_bccEmail = ""
	_subject = "TEST21"
	_text = "this is text"


	print (sentMail(_fromEmail, _toEmail, _subject, _text, _ccEmail, _bccEmail))
	print ("robert")

