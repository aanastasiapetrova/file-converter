import pytest
import sys
from tests.clients.fake_client import FakeClient
from tests.streams.fake_stream import FakeStream
from file_converter.commands import ConverterCommand
from file_converter.exceptions import InputMethodNotAllowedException, ConnectionIsFailedException, FormatIsUnsupportedException


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


def test_get_inputed_format_by_json_content(converter, json_file):
    """Test inputed data format getter by json file."""

    format = converter.get_inputed_data_format(json_file)
    assert format == 'json'


def test_get_inputed_format_by_rss_content(converter, rss_file):
    """Test inputed data format getter by rss file."""

    format = converter.get_inputed_data_format(rss_file)
    assert format == 'rss'


def test_get_inputed_format_by_atom_content(converter, atom_file):
    """Test inputed data format getter by atom file."""

    format = converter.get_inputed_data_format(atom_file)
    assert format == 'atom'


def test_get_inputed_data_format_by_text_fle_with_rss_content(converter, txt_file):
    """Test inputed data format getter by txt file with rss content."""

    format = converter.get_inputed_data_format(txt_file)
    assert format == 'rss'


def test_get_inputed_data_format_by_xml_file_with_atom_file(converter, xml_file):
    """Test inputed data format getter by xml file with atom content."""

    format = converter.get_inputed_data_format(xml_file)
    assert format == 'atom'


def test_get_inputed_data_format_by_incorrect_content(converter, text_file):
    """Test inputed data format getter raises exception in case of unrecognised format."""

    with pytest.raises(FormatIsUnsupportedException):
        converter.get_inputed_data_format(text_file)


def test_get_outputed_data_format_by_rss_file(converter):
    """Test outputed data format getter by rss file."""
    
    converter.output = 'test.rss'
    assert converter.get_output_data_format() == 'rss'

