import pytest
import os

from file_converter.managers.parsers_manager import parsers_manager 
from file_converter.managers.queries_manager import queries_manager
from file_converter.managers.adapters_manager import adapters_manager
from file_converter.managers.converters_manager import converters_manager

from file_converter.commands.converter_command import ConverterCommand
from .helpers.get_file import get_file
from file_converter.helpers.registrator import Registrator
from file_converter.helpers.data_getter import DataGetter
from file_converter.constants import FILES_TO_IGNORE

@pytest.fixture(autouse=True)
def register_modules():

        os.chdir('C:\\Users\\Anastasia\\Dev\\file-converter')

        cwd = os.path.abspath(os.getcwd())
        converter_dir = os.path.join(cwd, "file_converter")
        managers_dir = os.path.join(converter_dir, "managers")

        dirs_list = os.listdir(converter_dir)
        managers_list = os.listdir(managers_dir)
        dirs_to_register = []

        for path in managers_list:
            if os.path.isfile(os.path.join(managers_dir, path)) and path not in FILES_TO_IGNORE:
                dirs_to_register.append(path.split("_")[0])

        for path in dirs_list:
            if os.path.isdir(os.path.join(converter_dir, path)) and path in dirs_to_register:
                registrator = Registrator(os.path.join(converter_dir, path))
                registrator.register()

        os.chdir('C:\\Users\\Anastasia\\Dev\\file-converter\\tests')


@pytest.fixture
def data_getter():
    return DataGetter(None)


@pytest.fixture
def converter():
    return ConverterCommand(None, None)


@pytest.fixture
def json_query():
    return queries_manager.get("json")


@pytest.fixture
def rss_query():
    return queries_manager.get("rss")


@pytest.fixture
def atom_query():
    return queries_manager.get("atom")


@pytest.fixture
def json_adapter():
    return adapters_manager.get("json")


@pytest.fixture
def rss_adapter():
    return adapters_manager.get("rss")


@pytest.fixture
def atom_adapter():
    return adapters_manager.get("atom")


@pytest.fixture
def json_converter():
    return converters_manager.get("json")


@pytest.fixture
def rss_converter():
    return converters_manager.get("rss")


@pytest.fixture
def atom_converter():
    return converters_manager.get("atom")


@pytest.fixture
def file(request):
    return get_file(request.param)


@pytest.fixture
def parsed_json_data():
    data = get_file("fixtures/test.json")
    return parsers_manager.get("json").parse(data)


@pytest.fixture
def parsed_rss_data():
    data = get_file("fixtures/test.rss")
    return parsers_manager.get("rss").parse(data)


@pytest.fixture
def parsed_atom_data():
    data = get_file("fixtures/test.atom")
    return parsers_manager.get("atom").parse(data)


@pytest.fixture
def adapted_json_data(parsed_json_data, json_adapter):
    return json_adapter.adapt(parsed_json_data)


@pytest.fixture
def adapted_rss_data(parsed_rss_data, rss_adapter):
    return rss_adapter.adapt(parsed_rss_data)


@pytest.fixture
def adapted_atom_data(parsed_atom_data, atom_adapter):
    return atom_adapter.adapt(parsed_atom_data)

