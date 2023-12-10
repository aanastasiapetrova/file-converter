import pytest
from tests.clients.fake_client import FakeClient
from file_converter.commands import ConverterCommand
from file_converter.exceptions import InputMethodNotAllowed


@pytest.fixture
def converter():
    return ConverterCommand(None, None)


def test_get_inputed_data_from_absolute_file_path(converter):
    """Test inputed data getter by getting information from absolute file path."""

    converter.input = 'C:/Users/Anastasia/Dev/file-converter/tests/fixtures/test.json'
    assert converter.get_input_data() == ['{"id": 1, "title": "test", "text": "lorem ipsum dolor", "author": "unknown", "date": "2023-12-10"}']

def test_get_inputed_data_from_relative_file_path(converter):
    """Test inputed data getter by getting information from relative file path."""

    converter.input = 'fixtures/test.json'
    assert converter.get_input_data() == ['{"id": 1, "title": "test", "text": "lorem ipsum dolor", "author": "unknown", "date": "2023-12-10"}']

def test_get_inputed_data_from_remote_url_ended_by_domain(converter):
    """Test inputed data getter by getting information from ended by domain remote url."""

    converter.input = 'https://some-website.com'
    assert converter.get_input_data(FakeClient('Successfull!')) == 'Successfull!'

def test_get_inputed_data_from_remote_url_ended_by_nested_page(converter):
    """Test inputed data getter by getting information from ended by nested page remote url."""

    converter.input = 'http://some-website.com/rss'
    assert converter.get_input_data(FakeClient('Successfull!')) == 'Successfull!'


def test_get_inputed_data_by_unknown_way(converter):
    """Test inputed data getter by inputing unknown data type."""
    
    converter.input = 'unknown-way'

    with pytest.raises(InputMethodNotAllowed):
        converter.get_input_data()