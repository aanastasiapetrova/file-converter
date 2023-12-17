import pytest
from .helpers.get_file import get_file

@pytest.fixture
def from_json_to_json_file():
    return get_file('fixtures/from_json_to_json.json')


@pytest.fixture
def from_rss_to_json_file():
    return get_file('fixtures/from_rss_to_json.json')


@pytest.fixture
def from_atom_to_json_file():
    return get_file('fixtures/from_atom_to_json.json')


@pytest.fixture
def from_json_to_rss_file():
    return get_file('fixtures/from_json_to_rss.rss')


@pytest.fixture
def from_rss_to_rss_file():
    return get_file('fixtures/from_rss_to_rss.rss')


@pytest.fixture
def from_atom_to_rss_file():
    return get_file('fixtures/from_atom_to_rss.rss')


@pytest.fixture
def from_json_to_atom_file():
    return get_file('fixtures/from_json_to_atom.atom')


@pytest.fixture
def from_rss_to_atom_file():
    return get_file('fixtures/from_rss_to_atom.atom')


@pytest.fixture
def from_atom_to_atom_file():
    return get_file('fixtures/from_atom_to_atom.atom')


def test_convert_json_by_json_converter(adapted_json_data, json_converter, from_json_to_json_file):
    """Test json converter by json adapted file."""

    converted_data = json_converter.convert(adapted_json_data)

    assert converted_data == from_json_to_json_file


def test_convert_rss_by_json_converter(adapted_rss_data, json_converter, from_rss_to_json_file):
    """Test json converter by rss adapted file."""

    converted_data = json_converter.convert(adapted_rss_data)

    assert converted_data == from_rss_to_json_file


def test_convert_atom_by_json_converter(adapted_atom_data, json_converter, from_atom_to_json_file):
    """Test json converter by atom adapted file."""

    converted_data = json_converter.convert(adapted_atom_data)

    assert converted_data == from_atom_to_json_file


def test_convert_from_json_by_rss_converter(adapted_json_data, rss_converter, from_json_to_rss_file):
    """Test rss converter by json adapted file."""

    converted_data = rss_converter.convert(adapted_json_data)
    formatted_converted_data = " ".join([tag.strip() for tag in str(converted_data).split("\n")]).strip()

    assert formatted_converted_data == from_json_to_rss_file


def test_convert_from_rss_by_rss_converter(adapted_rss_data, rss_converter, from_rss_to_rss_file):
    """Test rss converter by rss adapted file."""

    converted_data = rss_converter.convert(adapted_rss_data)
    formatted_converted_data = " ".join([tag.strip() for tag in str(converted_data).split("\n")]).strip()
    
    assert formatted_converted_data == from_rss_to_rss_file


def test_convert_from_atom_by_rss_converter(adapted_atom_data, rss_converter, from_atom_to_rss_file):
    """Test rss converter by atom adapted file."""

    converted_data = rss_converter.convert(adapted_atom_data)
    formatted_converted_data = " ".join([tag.strip() for tag in str(converted_data).split("\n")]).strip()
    
    assert formatted_converted_data == from_atom_to_rss_file


def test_convert_from_json_by_atom_converter(adapted_json_data, atom_converter, from_json_to_atom_file):
    """Test atom converter by json adapted file."""

    converted_data = atom_converter.convert(adapted_json_data)
    formatted_converted_data = " ".join([tag.strip() for tag in str(converted_data).split("\n")]).strip()
    
    assert formatted_converted_data == from_json_to_atom_file


def test_convert_from_rss_by_atom_converter(adapted_rss_data, atom_converter, from_rss_to_atom_file):
    """Test atom converter by rss adapted file."""

    converted_data = atom_converter.convert(adapted_rss_data)
    formatted_converted_data = " ".join([tag.strip() for tag in str(converted_data).split("\n")]).strip()
    
    assert formatted_converted_data == from_rss_to_atom_file


def test_convert_from_atom_by_atom_converter(adapted_atom_data, atom_converter, from_atom_to_atom_file):
    """Test atom converter by atom adapted file."""

    converted_data = atom_converter.convert(adapted_atom_data)
    formatted_converted_data = " ".join([tag.strip() for tag in str(converted_data).split("\n")]).strip()
    
    assert formatted_converted_data == from_atom_to_atom_file