import pytest

import file_converter.parsers as parsers
import file_converter.queries as queries
import file_converter.adapters as adapters
import file_converter.converters as converters
from file_converter.commands import ConverterCommand
from .helpers.get_file import get_file


@pytest.fixture
def converter():
    return ConverterCommand(None, None)


@pytest.fixture
def json_query():
    return queries.query_manager.get_query("json")


@pytest.fixture
def rss_query():
    return queries.query_manager.get_query("rss")


@pytest.fixture
def atom_query():
    return queries.query_manager.get_query("atom")


@pytest.fixture
def json_adapter():
    return adapters.adapter_manager.get_adapter("json")


@pytest.fixture
def rss_adapter():
    return adapters.adapter_manager.get_adapter("rss")


@pytest.fixture
def atom_adapter():
    return adapters.adapter_manager.get_adapter("atom")


@pytest.fixture
def json_converter():
    return converters.converter_manager.get_converter("json")


@pytest.fixture
def rss_converter():
    return converters.converter_manager.get_converter("rss")


@pytest.fixture
def atom_converter():
    return converters.converter_manager.get_converter("atom")


@pytest.fixture
def json_file():
    return get_file("fixtures/test.json")


@pytest.fixture
def rss_file():
    return get_file("fixtures/test.rss")


@pytest.fixture
def atom_file():
    return get_file("fixtures/test.atom")


@pytest.fixture
def txt_file():
    return get_file("fixtures/test.txt")


@pytest.fixture
def xml_file():
    return get_file("fixtures/test.xml")


@pytest.fixture
def text_file():
    return get_file("fixtures/text.txt")


@pytest.fixture
def parsed_json_data():
    data = get_file("fixtures/test.json")
    return parsers.parsers_manager.get_parser("json").parse(data)


@pytest.fixture
def parsed_rss_data():
    data = get_file("fixtures/test.rss")
    return parsers.parsers_manager.get_parser("rss").parse(data)


@pytest.fixture
def parsed_atom_data():
    data = get_file("fixtures/test.atom")
    return parsers.parsers_manager.get_parser("atom").parse(data)


@pytest.fixture
def adapted_json_data(parsed_json_data, json_adapter):
    return json_adapter.adapt(parsed_json_data)


@pytest.fixture
def adapted_rss_data(parsed_rss_data, rss_adapter):
    return rss_adapter.adapt(parsed_rss_data)


@pytest.fixture
def adapted_atom_data(parsed_atom_data, atom_adapter):
    return atom_adapter.adapt(parsed_atom_data)
