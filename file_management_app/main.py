from flask import Flask, render_template, request, jsonify, send_from_directory

from werkzeug.routing import Rule
from werkzeug.utils import secure_filename

import os
import subprocess


CWD = os.path.join(os.getcwd(), 'file_management_app')
UPLOAD_FOLDER = os.path.join(CWD, 'uploaded_files/')  # Folder where uploaded files will be stored

app = Flask(__name__)
PORT = 5001


def _get_file_information(filename):
    # Get file information returned by bash command 'file'
    # User 'wsl' (windows subsystem for linux) to run the 'file' bash command. =
    # Since my docker container is using linux jammy distribution, I am using file command directly
    # command = ['wsl','file', file_path]
    # This is part 1 of assignment to provide information of the file after it is uploaded
    command = ['file', os.path.join(UPLOAD_FOLDER, filename)]
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Information has "Full file-path: File-information". We don't need "Full file-path".
        bash_file_output = result.stdout.split(':')[-1]
    except Exception as e:
        print("Failed to get file information")
        bash_file_output = "Failed to Fetch Type."
        print("Sorry, wasn't able to fetch file-information of uploaded file. ERROR:" + str(e))
    return {
        "filename": filename,
        "file_info": bash_file_output + " , " + "size: " + str(os.path.getsize(os.path.join(UPLOAD_FOLDER, filename)))
    }


@app.route('/')
def index():
    result = list_uploaded_files()
    return render_template('index.html', file_list = result)


@app.route('/v1', methods=['GET'])
def list_endpoints():
    endpoints = []
    for rule in app.url_map.iter_rules():
        if isinstance(rule, Rule):
            endpoints.append(rule.rule)
    return jsonify({"endpoints": endpoints})


@app.route('/v1/list_files', methods=['GET'])
def list_uploaded_files():
    try:
        uploaded_files = os.listdir(UPLOAD_FOLDER)
        print('Uploaded files', uploaded_files)
        return jsonify({"uploaded_files": uploaded_files})
    except Exception as e:
        return jsonify({"ERROR": "An error occurred while listing uploaded files"})


@app.route('/v1/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({"ERROR": "No file part"})
        file = request.files['file']
        if file.filename == '':
            return jsonify({"ERROR": "No selected file"})
        filename = file.filename

        file.save(UPLOAD_FOLDER + filename)
        file_info = _get_file_information(filename)
        return jsonify({"message": "File: " + filename + " uploaded successfully", "file_info": file_info})
    except Exception as e:
        return jsonify({"ERROR": "An error occurred while processing the file" + e})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001)
