import io
import os
from flask import render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
from app import app
from PIL import Image
from io import BytesIO
import os
import imghdr
import uuid


def neiro(filepath):
    pass



def generate_random_filename(extension):
    """Генерация случайного имени файла с указанным расширением."""
    return f"{uuid.uuid4()}.{extension}"

@app.route('/process_image', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        file_bytes = file.read()
        file_type = imghdr.what(None, h=file_bytes)

        if file_type in ['jpeg', 'png', 'jpg']:
            filename = generate_random_filename(file_type)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.seek(0)
            file.save(file_path)
            #neiro(filepath) -> filepath
            return jsonify({"message": "File saved successfully!", "file_path": file_path}), 200
        else:
            return jsonify({"error": "Unsupported file type"}), 400


@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404


@app.errorhandler(500)
def err_inside():
    return render_template('500.html'), 500
