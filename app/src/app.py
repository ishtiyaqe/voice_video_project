import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from src.utils.video_utils import get_whisper_srt

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.template_folder = "templates"

    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")

    @app.route("/upload", methods=["POST"])
    def upload_file():
        project_id = request.form["project_id"]
        file = request.files["audio_file"]
        if file:
            audio_bytes = file.read()
            result = get_whisper_srt(f_name=project_id, audio_bytes=audio_bytes)
            return jsonify({
                "project_id": project_id,
                "status": "MEDIA_SRT_CREATED",
                "transcript": result
            })
        return "No file uploaded", 400

    @app.route("/build_srt_file/<project_id>", methods=["POST"])
    def build_srt_file(project_id):
        audio_bytes = request.data
        result = get_whisper_srt(f_name=project_id, audio_bytes=audio_bytes)
        return jsonify({
            "project_id": project_id,
            "status": "MEDIA_SRT_CREATED",
            "transcript": result
        })

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
