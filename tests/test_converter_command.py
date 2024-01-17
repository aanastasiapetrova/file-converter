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
