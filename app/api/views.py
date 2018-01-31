from flask import render_template, redirect, url_for, session

from app.api import api_bp
from app.api.forms.word_count_form import WordCountForm


@api_bp.route('/', methods=['POST', 'GET'])
def word_count():
    session.pop('word_count_response', None)
    form = WordCountForm()
    if form.validate_on_submit():
        text = form.text.data
        session['text'] = text
        session['word_count'] = 0
        session['word_count_response'] = True
    else:
        session['errors'] = form.errors
    return render_template('word_count.html', form=form)
