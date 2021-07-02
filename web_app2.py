from flask import Flask,render_template,url_for,request
from flaskext.markdown import Markdown
import re
import pandas as pd
import spacy
from spacy import displacy
import en_core_web_sm
nlp = spacy.load('en_core_web_sm')

app = Flask(__name__)
Markdown(app)

HTML_WRAPPER = """
<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>
"""

@app.route('/')
def index():
	results = ""
	return render_template("index2.html", results=results)

@app.route('/process',methods=["GET", "POST"])
def process():
	if request.method =='POST':
		rawtext = request.form['rawtext']
		doc = nlp(rawtext)
		html = displacy.render(doc,style="ent")
		html = html.replace("\n\n","\n")
		results = HTML_WRAPPER.format(html)
	
	return render_template("index2.html",results=results)

if __name__ == '__main__':
	app.run(debug=True)