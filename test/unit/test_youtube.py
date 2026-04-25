from test.unit import client
from unittest import mock

@mock.patch('flaskr.main.download_youtube')
def test_youtube_good_args(mock_yt_dl, client):
    response = client.post('/youtube', data= {
        "directory": "/path/to/good/directory",
        "url": "https://www.youtube.com/watch?v=TbhDIlbj64Q",
        "audio_bool": False
    })
    assert response.status_code == 201
    assert response.json["message"] == None

def test_youtube_bad_url(client):
    response = client.post('/youtube', data= {
        "directory": "/path/to/good/directory",
        "url": "bad_url",
        "audio_bool": False
    })
    assert response.status_code == 400
    assert 'bad url' in response.json["message"]['url']

def test_youtube_no_url(client):
    response = client.post('/youtube', data= {
        "directory": "/path/to/good/directory",
        "audio_bool": False
    })
    assert response.status_code == 400
    assert 'no url' in response.json["message"]['url']
