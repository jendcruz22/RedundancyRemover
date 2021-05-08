import os
import shutil
import urllib.request
from flask import Flask, flash, send_file, request, redirect, render_template
from werkzeug.utils import secure_filename
from PIL import Image
import imagehash
import numpy as np

dirname = "photos"
UPLOAD_FOLDER = 'C:/Users/jencr/OneDrive/Documents/GitHub/RedundancyRemover/photos'

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	

@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['GET','POST'])
def upload_file():
	for filename in os.listdir(dirname):
		file_path = os.path.join(dirname, filename)
		try:
			if os.path.isfile(file_path) or os.path.islink(file_path):
				os.unlink(file_path)
			elif os.path.isdir(file_path):
				shutil.rmtree(file_path)
		except Exception as e:
			print('Failed to delete %s. Reason: %s' % (file_path, e))
	if os.path.exists("results.zip"):
		os.remove("results.zip")

	if request.method == 'POST':
        # check if the post request has the files part
		if 'files[]' not in request.files:
			flash('No file part')
			return redirect(request.url)
		files = request.files.getlist('files[]')

		for file in files:
			if file and allowed_file(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		
		fnames = os.listdir(dirname)
		hashes = {}
		copies = []
		hash_size = 8

		flash("Finding copies Now!\n")
		for image in fnames:
			with Image.open(os.path.join(dirname,image)) as img:
				temp_hash = imagehash.average_hash(img, hash_size)
				if temp_hash in hashes:
					flash("Copy {} \nfound for Image {}!\n".format(image,hashes[temp_hash]))
					copies.append(image)
				else:
					hashes[temp_hash] = image
		
		if len(copies) != 0:
			for copy in copies:
				os.remove(os.path.join(dirname,copy))
				flash("{} Deleted Succesfully!".format(copy))

		else:
			flash("No copies Found :(")
			
		shutil.make_archive('results', 'zip', 'photos')
		# extract the text and display it
		return render_template('upload.html')

	elif request.method == 'GET':
		return render_template('upload.html')

		# return redirect('/')

@app.route('/alldownloads')
def alldownloads():
	path = "results.zip"
	return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)