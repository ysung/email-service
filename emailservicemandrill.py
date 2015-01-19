import mandrill

class EmailServiceMandrill:
	def send(self, fromEmail, toEmail, subject, text, ccEmail = [], bccEmail = []):
		mandrill_client = mandrill.Mandrill('27ZpDc-XlF0bkiaWhIYqBQ')
		message = {
		'from_email': fromEmail,
		'to':[],
		'test': text,
		'subject': subject
		}

		if type(toEmail) == str:
			toEmail = [toEmail]
		for item in toEmail:
					message['to'] += [{'email': item, 'type': 'to'}]

		if type(ccEmail) == str:
			ccEmail = [ccEmail]
		for item in ccEmail:
					message['to'] += [{'email': item, 'type': 'cc'}]
		
		if type(bccEmail) == str:
			bccEmail = [bccEmail]
		for item in bccEmail:
					message['to'] += [{'email': item, 'type': 'bcc'}]  

		result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool')
		status = 0 if result[0]['status'] == 'sent' else 1
		return status

# test = EmailServiceMandrill()
# result = test.send('s.yunchieh@gmail.com', 's.yunchieh@gmail.com',
# 		subject = "Test9", text = "testset123")
# print (result) 


"""


try:
    mandrill_client = mandrill.Mandrill('27ZpDc-XlF0bkiaWhIYqBQ')
    message = {'attachments': [{'content': 'ZXhhbXBsZSBmaWxl',
                      'name': 'myfile.txt',
                      'type': 'text/plain'}],
     # 'auto_html': None,
     # 'auto_text': None,
     'bcc_address': 'message.bcc_address@example.com',
     'from_email': 's.yunchieh@gmail.com',
     'from_name': 'Jasper',
     # 'global_merge_vars': [{'content': 'merge1 content', 'name': 'merge1'}],
     # 'google_analytics_campaign': 'message.from_email@example.com',
     # 'google_analytics_domains': ['example.com'],
     # 'headers': {'Reply-To': 'message.reply@example.com'},
     # 'html': '<p>Example HTML content</p>',
     # 'images': [{'content': 'ZXhhbXBsZSBmaWxl',
     #             'name': 'IMAGECID',
     #             'type': 'image/png'}],
     # 'important': False,
     # 'inline_css': None,
     # 'merge': True,
     # 'merge_language': 'mailchimp',
     # 'merge_vars': [{'rcpt': 'recipient.email@example.com',
     #                 'vars': [{'content': 'merge2 content', 'name': 'merge2'}]}],
     # 'metadata': {'website': 'www.example.com'},
     # 'preserve_recipients': None,
     # 'recipient_metadata': [{'rcpt': 'recipient.email@example.com',
                             # 'values': {'user_id': 123456}}],
     # 'return_path_domain': None,
     # 'signing_domain': None,
     # 'subaccount': 'customer-123',
     'subject': 'TEST123',
     # 'tags': ['password-resets'],
     'text': 'Example text content',
     'to': [{'email': 'cuitjason@hotmail.com',
             'name': 'Sungyy',
             'type': 'to'}]}
     # 'track_clicks': None,
     # 'track_opens': None,
     # 'tracking_domain': None,
     # 'url_strip_qs': None,
     # 'view_content_link': None}
    result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool')
    '''
    [{'_id': 'abc123abc123abc123abc123abc123',
      'email': 'recipient.email@example.com',
      'reject_reason': 'hard-bounce',
      'status': 'sent'}]
    '''

except mandrill.Error as e:
    # Mandrill errors are thrown as exceptions
    print('A mandrill error occurred: {} - {}'.format(e.__class__, e))
    # A mandrill error occurred: <class 'mandrill.UnknownSubaccountError'> - No subaccount exists with the id 'customer-123'    
    raise
"""