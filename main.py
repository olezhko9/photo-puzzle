import os
from flask import Flask, request, redirect, send_from_directory, jsonify
from werkzeug.utils import secure_filename
from mosaic.PhotoPuzzle import PhotoPuzzle
from flask_cors import CORS

mode = os.environ.get("FLASK_ENV", default='dev')

UPLOAD_DIR = './uploads/'

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)


@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(UPLOAD_DIR, filename)


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        else:
            file = request.files['file']
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_DIR, filename))
            photo_path = os.path.abspath(UPLOAD_DIR + filename)
            folder = os.path.abspath('mosaic/tiles/')
            puzzle = PhotoPuzzle(photo_path, folder)
            saved_file = puzzle.create_photo_puzzle(pix_to_tile=8, njobs=-1).split(os.sep)[-1]
            print(saved_file)
            response = {'filename': saved_file}
            return jsonify(response)


if __name__ == '__main__':
    host = "0.0.0.0"
    app.run(host=host, debug=True)
