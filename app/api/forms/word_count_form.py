from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

class WordCountForm(FlaskForm):
    text = StringField('Please enter input text:', validators=[
        DataRequired()
    ], widget=TextArea())
