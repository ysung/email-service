from flask.ext.wtf import Form
from wtforms import TextField, StringField, BooleanField, validators
from wtforms.fields.html5 import EmailField

# from wtforms.validators import DataRequired

class EmailsServiceForm(Form):
	from_email = EmailField('from_email', [validators.Length(min=6, max=120), validators.Email()])
	to_email = EmailField('to_email', [validators.Length(min=6, max=120), validators.Email()])



	# cc_email = StringField('cc_email', validators=[DataRequired()])
	# bcc_email = StringField('bcc_email', validators=[DataRequired()])
