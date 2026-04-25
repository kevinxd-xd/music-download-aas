from wtforms import Form, BooleanField, StringField, PasswordField, validators

class YoutubeForm(Form):
    # TODO: override this validator to focus only on youtube links
    url = StringField('url', validators=[validators.url(message="bad url"), validators.InputRequired(message="no url")])
    audio_bool = BooleanField('audio_only', validators=[validators.InputRequired(message="no bool")])
    directory = StringField('directory_path', validators=[validators.InputRequired(message="no dir")])