import pytest
from file_converter.commands import ConverterCommand
import file_converter.parsers as parsers
import file_converter.queries as queries


@pytest.fixture
def converter():
    return ConverterCommand(None, None)


@pytest.fixture
def json_query():
    return queries.query_manager.get_query('json')


@pytest.fixture
def rss_query():
    return queries.query_manager.get_query('rss')


@pytest.fixture
def atom_query():
    return queries.query_manager.get_query('atom')


@pytest.fixture
def json_file():
    with open('fixtures/test.json', 'r', encoding='utf8') as filename:
        data = ' '.join([l.strip() for l in filename.readlines()])
    return data


@pytest.fixture
def rss_file():
    with open('fixtures/test.rss', 'r', encoding='utf8') as filename:
        data = ' '.join([l.strip() for l in filename.readlines()])
    return data


@pytest.fixture
def atom_file():
    with open('fixtures/test.atom', 'r', encoding='utf8') as filename:
        data = ' '.join([l.strip() for l in filename.readlines()])
    return data


@pytest.fixture
def txt_file():
    with open('fixtures/test.txt', 'r', encoding='utf8') as filename:
        data = ' '.join([l.strip() for l in filename.readlines()])
    return data


@pytest.fixture
def xml_file():
    with open('fixtures/test.xml', 'r', encoding='utf8') as filename:
        data = ' '.join([l.strip() for l in filename.readlines()])
    return data


@pytest.fixture
def text_file():
    with open('fixtures/text.txt', 'r', encoding='utf8') as filename:
        data = ' '.join([l.strip() for l in filename.readlines()])
    return data


@pytest.fixture
def parsed_json_data():
    with open('fixtures/test.json', 'r', encoding='utf8') as filename:
        data = ' '.join([l.strip() for l in filename.readlines()])
    return parsers.parsers_manager.get_parser('json').parse(data)


@pytest.fixture
def parsed_rss_data():
    with open('fixtures/test.rss', 'r', encoding='utf8') as filename:
        data = ' '.join([l.strip() for l in filename.readlines()])
    return parsers.parsers_manager.get_parser('rss').parse(data)


@pytest.fixture
def parsed_atom_data():
    with open('fixtures/test.atom', 'r', encoding='utf8') as filename:
        data = ' '.join([l.strip() for l in filename.readlines()])
    return parsers.parsers_manager.get_parser('atom').parse(data)