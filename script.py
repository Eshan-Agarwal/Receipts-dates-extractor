#importing libraries
import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request,redirect
from preprocess import process_image_for_ocr
import pandas as pd
import shutil
from remove import remove





#creating instance of the class
app=Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))



#to tell flask what url shoud trigger the function index()
@app.route("/")
def index():
    return flask.render_template('index.html')



@app.route("/upload",methods=["POST"])
def upload():
	if request.method == 'POST':
		target = os.path.join(APP_ROOT, 'receipts/')
		print(target)

		if not os.path.isdir(target):
			os.mkdir(target)


		for file in request.files.getlist("file"):
			print(file)
			filename = file.filename
			destination = "/".join([target, filename])
			print(destination)
			file.save(destination)
		
		your_path = target

		# open every image path store in images directory 

		for root, dirs, files in os.walk(target, topdown=False):

				# Make DataFrame to show final result as in form of dataframe
				
				df = pd.DataFrame(columns = ['name','date_time'])
				for name in files:
						path = os.path.join(root, name)
						print(name)

						name = name
						a =  process_image_for_ocr(path)
						df = df.append(
								dict(
									 name = name,
									 date_time = a
									),ignore_index = True)

		shutil.rmtree(target)
		return render_template("result.html",tables=[df.to_html(classes='data', header="true")],imgpath = path)
if __name__ == "__main__":
	app.run(port=4555, debug=True)


