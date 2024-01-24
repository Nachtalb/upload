from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from pathlib import Path
import string
import random

app = Flask(__name__)

# Directory for storing uploaded files
UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

API_KEYS_FILE = Path("api_keys.txt")
# Maximum file size in bytes (50 MB)
MAX_FILE_SIZE = 50 * 1024 * 1024


def api_key_exists(api_key):
    return api_key in set(filter(None, API_KEYS_FILE.read_text().splitlines()))


@app.route("/")
def index():
    return render_template("index.html")


def generate_random_id(length=10):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


@app.route("/upload", methods=["POST"])
def upload_file():
    api_key = request.form.get("api_key", "")

    if not api_key or not api_key_exists(api_key):
        return jsonify({"error": "Invalid or missing API key"}), 403

    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]

    if file.content_length > MAX_FILE_SIZE:
        return jsonify({"error": "File too large"}), 413

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file:
        file_id = generate_random_id()
        suffix = Path(secure_filename(file.filename)).suffix
        file_path = (UPLOAD_FOLDER / file_id).with_suffix(suffix)
        while file_path.exists():
            file_path = file_path.with_name(generate_random_id())

        file.save(file_path)

        # Return the URL for the uploaded file
        file_url = request.host_url + "files/" + file_path.name
        return jsonify({"url": file_url}), 201


@app.route("/files/<filename>")
def uploaded_file(filename):
    # Is this secure?
    # YES: https://stackoverflow.com/questions/20646822/how-to-secure-files-in-flask-upload-folder
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


# Placeholder for health/info endpoint
@app.route("/info", methods=["GET"])
def info():
    files_count = len(list(UPLOAD_FOLDER.glob("*")))
    storage_space = sum(f.stat().st_size for f in UPLOAD_FOLDER.glob("*"))
    return jsonify({"files_count": files_count, "storage_space": storage_space}), 200


if __name__ == "__main__":
    app.run(debug=True)
