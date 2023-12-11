import pytest
import sys
from tests.clients.fake_client import FakeClient
from tests.streams.fake_stream import FakeStream
from file_converter.commands import ConverterCommand
from file_converter.exceptions import InputMethodNotAllowedException, ConnectionIsFailedException


@pytest.fixture
def converter():
    return ConverterCommand(None, None)


def test_get_inputed_data_from_absolute_file_path(converter):
    """Test inputed data getter by getting information from absolute file path."""

    converter.input = 'C:/Users/Anastasia/Dev/file-converter/tests/fixtures/test.json'
    assert converter.get_input_data() == ('{"id": 1, "title": "test", "text": "lorem ipsum dolor", "author": "unknown", "date": "2023-12-10"}', 'json')


def test_get_inputed_data_from_relative_file_path(converter):
    """Test inputed data getter by getting information from relative file path."""

    converter.input = 'fixtures/test.json'
    assert converter.get_input_data() == ('{"id": 1, "title": "test", "text": "lorem ipsum dolor", "author": "unknown", "date": "2023-12-10"}', 'json')


def test_get_inputed_data_from_remote_url_ended_by_domain(converter):
    """Test inputed data getter by getting information from ended by domain remote url."""

    converter.input = 'https://some-website.com'
    assert converter.get_input_data(client=FakeClient('{"id": 1}')) == ('{"id": 1}', 'json')


def test_get_inputed_data_from_remote_url_ended_by_nested_page(converter):
    """Test inputed data getter by getting information from ended by nested page remote url."""

    converter.input = 'http://some-website.com/rss'
    assert converter.get_input_data(client=FakeClient('{"id": 1}')) == ('{"id": 1}', 'json')


def test_get_inputed_data_from_stdin(converter):
    """Test inputed data getter by getting information by stdin."""
    converter.input = 'stdin'
    assert converter.get_input_data(stream=FakeStream('{"id": 1}')) == ('{"id": 1}', 'json')


def test_get_inputed_data_by_unknown_method(converter):
    """Test inputed data getter by inputing unknown data type."""

    converter.input = 'unknown-method'

    with pytest.raises(InputMethodNotAllowedException):
        converter.get_input_data()


def test_get_inputed_data_with_connection_error(converter):
    """Test inputed data getter handling connection error."""
    
    converter.input = 'http://unexisted-url.ru'

    with pytest.raises(ConnectionIsFailedException):
        converter.get_input_data('Failure')