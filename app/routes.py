import os
from flask import render_template, request, jsonify
from werkzeug.utils import secure_filename
from app import app


@app.route('/process_image', methods=['POST'])
def process_image():
    if 'files' not in request.files:
        return jsonify({'status': 'error', 'message': 'Файл не был выбран!'})

    file = request.files['files']

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Вызов функции обработки нейронкой
        # answ = foo(filepath)
        answ = 'бебрачка'

        return jsonify({'status': 'success', 'message': answ})

    return jsonify({'status': 'error', 'message': f'Недопустимый тип файла! {file.filename}'})

@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404


@app.errorhandler(500)
def err_inside():
    return render_template('500.html'), 500
