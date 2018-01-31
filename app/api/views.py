from flask import render_template
from app.api import api_bp

@api_bp.route('/')
def api():
    return render_template('wc.html')
