from flask_wtf import Form
from wtforms import StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

class WordCountForm(Form):
    text = StringField('Please enter a body of text:', validators=[
        DataRequired()
    ], widget=TextArea())
