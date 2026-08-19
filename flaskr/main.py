from flask import Flask, request
import os

from flaskr.core.utils import Utils
from flaskr.core.config_builder import ConfigBuilder
from flaskr.core.yt_dlp import download_youtube
from flaskr.model.youtube_form import YoutubeForm

BASE_DIRECTORY = "/mnt/media/music"

app = Flask(__name__)

@app.route("/directories", methods=['GET'])
def music_directories():
    try:
        directories = Utils.get_directories()
        return {
            "directories": directories,
            "message": "Success",
            "status": 200
        }, 200
    except Exception as e:
        print(e)
        return {
            "directories": None,
            "message": e,
            "status": 400
        }, 400


@app.route("/youtube", methods=['POST'])
def init_yt():
    youtube_form = YoutubeForm(request.form)
    if youtube_form.validate():
        config = ConfigBuilder()
        # TODO: write custom validator https://wtforms.readthedocs.io/en/3.0.x/validators/#custom-validators
        # need url and directory sanitizers
        url = youtube_form.data.get('url')
        audio_bool = youtube_form.data.get('audio_bool')
        directory = os.path.join(BASE_DIRECTORY, youtube_form.data.get('directory'))
        try:
            config.set_format(audio_only=audio_bool)
            config.set_path(directory)
            ydl_opts = config.get_options()
            download_youtube(url, ydl_opts)
        except Exception as e:
            print(e)
            return {
                "status": 400,
                "message": "Something went wrong."
            }, 400
        return {
            "status": 201,
            "message": "Successfully downloaded song"
        }, 201
    else:
        print(youtube_form.errors)
        return {
            "status": 400,
            "message": youtube_form.errors
        }, 400