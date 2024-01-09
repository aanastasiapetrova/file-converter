import os

import pytest

from file_converter.exceptions import (
    ConnectionIsFailedException,
    FormatIsUnsupportedException,
    InputMethodNotAllowedException,
)
from tests.clients.fake_client import FakeClient
from tests.streams.fake_stream import FakeStream


@pytest.mark.parametrize(
        "file,path",
        [
            ("fixtures/test.json", os.path.abspath("fixtures/test.json")),
            ("fixtures/test.json", "fixtures/test.json")
        ],
        indirect=["file",]
    )
def test_get_inputed_data_from_file_path(converter, file, path):
    """Test inputed data getter by getting information from relative or absolute file path."""

    converter.input = path
    assert converter.get_input_data() == (file, "json")


@pytest.mark.parametrize("url", ["https://some-website.com", "http://some-website.com/rss"])
def test_get_inputed_data_from_remote_url(converter, url):
    """Test inputed data getter by getting information from remote url."""

    converter.input = url
    assert converter.get_input_data(client=FakeClient('{"id": 1}')) == (
        '{"id": 1}',
        "json",
    )


def test_get_inputed_data_from_stdin(converter):
    """Test inputed data getter by getting information by stdin."""
    converter.input = "stdin"
    assert converter.get_input_data(stream=FakeStream('{"id": 1}')) == (
        '{"id": 1}',
        "json",
    )


def test_get_inputed_data_by_unknown_method(converter):
    """Test inputed data getter by inputing unknown data type."""

    converter.input = "unknown-method"

    with pytest.raises(InputMethodNotAllowedException):
        converter.get_input_data()


def test_get_inputed_data_with_connection_error(converter):
    """Test inputed data getter handling connection error."""

    converter.input = "http://unexisted-url.ru"

    with pytest.raises(ConnectionIsFailedException):
        converter.get_input_data("Failure")


@pytest.mark.parametrize(
        "file,expected",
        [
            ("fixtures/test.json", "json"),
            ("fixtures/test.rss", "rss"),
            ("fixtures/test.atom", "atom"),
            ("fixtures/test.txt", "rss"),
            ("fixtures/test.xml", "atom")
        ],
        indirect=["file",]
)
def test_get_inputed_format_by_json_content(converter, file, expected):
    """Test inputed data format getter by json file."""

    format = converter.get_inputed_data_format(file)
    assert format == expected


@pytest.mark.parametrize(
        "file",
        ["fixtures/text.txt"],
        indirect=["file",]
)
def test_get_inputed_data_format_by_incorrect_content(converter, file):
    """Test inputed data format getter raises exception in case of unrecognised format."""

    with pytest.raises(FormatIsUnsupportedException):
        converter.get_inputed_data_format(file)


def test_get_outputed_data_format_by_rss_file(converter):
    """Test outputed data format getter by rss file."""

    converter.output = "test.rss"
    assert converter.get_output_data_format() == "rss"
