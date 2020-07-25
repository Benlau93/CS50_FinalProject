"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
import toxic_processing as process
from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def index():
    # render homepage
    return render_template("index.html")


@app.route("/result",methods=["POST"])
def result():
	if request.method=="POST":
		test = request.form.get("toxic-text")
		# process text
		test = process.preprocess_text(test)
		# tokenize
		test = process.tokenize(test)
		# get prediction
		result = process.predict(test)
		# additional parameters
		max_prob = max(result.values())
		toxic = max_prob >50
		return render_template("result.html",result = result,toxic=toxic,max_prob = max_prob)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST,PORT)
