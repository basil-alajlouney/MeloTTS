from flask import Flask, request, send_file
from flask_cors import CORS
from helper import tts_to_audio, jobs
import threading
from uuid import uuid4

def create_app():
    app = Flask(__name__)

    CORS(app)

    @app.route("/make_job", methods=["POST"])
    def default():
        uid = str(uuid4())
        text = request.get_json()["text"]
        threading.Thread(target=tts_to_audio, args=(text, uid)).start()
        return uid

    @app.route("/get_job")
    def get_job():
        job_id = request.args.get("job_id", None)
        
        if job_id is None:
            raise Exception("job id is required")
        
        audio = jobs.get(job_id, None)
        
        if audio is None:
            return None
        
        del jobs[job_id]
        
        return send_file(audio, mimetype="audio/wav", as_attachment=True, download_name="output.wav")

    return app