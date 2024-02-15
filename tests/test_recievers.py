import pytest
import os

from tests.clients.fake_client import FakeClient
from tests.streams.fake_stream import FakeStream

@pytest.mark.parametrize(
        "file,path",
        [
            ("fixtures/test.json", os.path.abspath("fixtures/test.json")),
            ("fixtures/test.json", "fixtures/test.json")
        ],
        indirect=["file", ]
)
def test_file_reciever_recieve_data(file_reciever, file, path):
    file_reciever.path = path

    assert file_reciever.recieve() == file


@pytest.mark.parametrize(
    "url",
    [
        "https://some-website.com",
        "http://some-website.com/rss"
    ]
)
def test_url_reciever_recieve_data(url_reciever, url):
    url_reciever.url = url
    url_reciever.client = FakeClient('{"id": 1}')

    assert url_reciever.recieve() == '{"id": 1}'


def test_stream_reciever_recieve_data(stream_reciever):
    stream_reciever.inputed_stream = "stdin"
    stream_reciever.stream = FakeStream('{"id": 1}')

    assert stream_reciever.recieve() == '{"id": 1}'