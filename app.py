from __future__ import unicode_literals
from flask import Flask,render_template,url_for,request

from nltk_summarization import nltk_summarizer

app = Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html')


@app.route('/analyze',methods=['GET','POST'])
def analyze():
	if request.method == 'POST':
		rawtext = request.form['rawtext']
		final_summary = nltk_summarizer(rawtext)
	return render_template('index.html',ctext=rawtext,final_summary=final_summary)



@app.route('/about')
def about():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)