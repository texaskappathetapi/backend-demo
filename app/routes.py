from datetime import datetime
from app.models import ShortURLs
from app import app, db
from flask import render_template, request, flash, redirect, url_for
from random import choice
import string

def generate_short_id(num_chars):
  return ''.join(choice(string.ascii_lowercase+string.ascii_uppercase+string.digits) for _ in num_chars)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # implement the POST method here!
        continue

    return render_template('index.html')


@app.route('/<short_id>')
def redirect_url(short_id):
    # implement the GET method for the short_ids here!
    pass
