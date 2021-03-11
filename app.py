from flask import Flask, render_template, session, redirect, request
from twitter_utils import get_request_token, get_oauth_verifier_url, get_access_token

app = Flask(__name__)
app.secret_key = '1234'

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/login/twitter')
def twitter_login():
    request_token = get_request_token()
    session['request_token'] = request_token

    return redirect(get_oauth_verifier_url(request_token))

@app.route('/auth/twitter')
def twitter_auth():
    oauth_verifier = request.args.get('oauth_verifier')
    access_token = get_access_token(session['request_token'], oauth_verifier)

app.run(port=4995)