import requests

class EmailServiceMailGun:
	def send(self, fromEmail, toEmail, subject, text, ccEmail = [], bccEmail = []):
		message = {"from": fromEmail, 
	  			   "to": toEmail,
      			   "subject": subject,
      			   "text": text,
      			   "cc": ccEmail,
      			   "bcc": bccEmail
      			   }
		result = requests.post( 
			"https://api.mailgun.net/v2/sandbox98ccd8ddccb641988f6e04bde006e722.mailgun.org/messages",
		    auth = ("api", "key-09270647a871aa0b1ce2d05988017414"),
		    data = message
		)

		status = 0 if result.status_code == 200 else 1
		return status

# test = EmailServiceMailGun()
# result = test.send('s.yunchieh@gmail.com', 'ysung@ucdavis.edu', ccEmail ='cuitjason@hotmail',
# 		subject = "Test15", text = "test")

# print (result)

'''
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v2/sandbox98ccd8ddccb641988f6e04bde006e722.mailgun.org/messages",
        auth=("api", "key-09270647a871aa0b1ce2d05988017414"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox98ccd8ddccb641988f6e04bde006e722.mailgun.org>",
              "to": "Yun-Chieh Sung <s.yunchieh@gmail.com>",
              "subject": "Hello Yun-Chieh Sung",
              "text": "Congratulations Yun-Chieh Sung, you just sent an email with Mailgun!  You are truly awesome!  You can see a record of this email in your logs: https://mailgun.com/cp/log .  You can send up to 300 emails/day from this sandbox server.  Next, you should add your own domain so you can send 10,000 emails/month for free."})

def send_complex_message():
    return requests.post(
        "https://api.mailgun.net/v2/sandbox98ccd8ddccb641988f6e04bde006e722.mailgun.org/messages",
        #auth=("api", "YOUR_API_KEY"),
        auth = ("api", "key-09270647a871aa0b1ce2d05988017414"),
        # files=[("attachment", open("files/test.jpg")),
        #        ("attachment", open("files/test.txt"))],
        data={"from": "Jasper <s.yunchieh@gmail.com>",
              "to": "cuitjason@hotmail.com",
              # "cc": "baz@example.com",
              # "bcc": "bar@example.com",
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!",
              "html": "<html>HTML version of the body</html>"})

if __name__ == "__main__":
	send_simple_message()
	send_complex_message()
'''
