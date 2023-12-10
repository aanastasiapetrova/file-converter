import pytest
from file_converter.managers import CommandManager
from file_converter.exceptions import OptionFormatException

@pytest.fixture
def command_line():
    return [
        'manage.py',
        'converter',
        '--input=test.rss',
        '--output=test.json',
        '--sort=asc',
        '--author=somebody',
        '--limit=1'
        ]


@pytest.fixture
def command_line_with_random_order():
    return [
        'manage.py',
        'converter',
        '--output=test.json',
        '--input=test.rss',
        '--author=somebody',
        '--sort=asc',
        '--limit=1'
        ]


@pytest.fixture
def command_line_with_mistake():
    return [
        'manage.py',
        'converter',
        '--output=test.json',
        '-input=test.rss',
        '--author=somebody',
        '--sort=asc',
        '--limit=1'
        ]


@pytest.fixture
def command_line_with_spaces():
    return [
        'manage.py',
        'converter',
        '--output=test.json',
        '--input=test.rss',
        '--author=first_name',
        'second_name',
        'last_name',
        '--sort=asc',
        '--limit=1'
        ]


@pytest.fixture
def command_args_parameters():
    return {
        'converter': {
            'input': None,
            'output': None,
            'sort': None,
            'author': None,
            'limit': None,
            },
        }


def test_initialize_args(command_line, command_args_parameters):
    """Test transform options to dict method with straight order of options."""

    command_manager = CommandManager(command_line[1], command_line[2:])
    command_details = command_manager.initialize_args(command_args_parameters[command_manager.command])
    assert command_details == {
        'input': 'test.rss',
        'output': 'test.json',
        'sort': 'asc',
        'author': 'somebody',
        'limit': '1'
    }


def test_initialize_args_with_random_order(command_line_with_random_order, command_args_parameters):
    """Test transform options to dict method with random order of options."""

    command_manager = CommandManager(command_line_with_random_order[1], command_line_with_random_order[2:])
    command_details = command_manager.initialize_args(command_args_parameters[command_manager.command])
    assert command_details == {
        'input': 'test.rss',
        'output': 'test.json',
        'sort': 'asc',
        'author': 'somebody',
        'limit': '1'
    }


def test_initialize_args_with_spaces(command_line_with_spaces, command_args_parameters):
    """Test transform options to dict method failure in case of inputed spaces in command option."""

    command_manager = CommandManager(command_line_with_spaces[1], command_line_with_spaces[2:])
    command_details = command_manager.initialize_args(command_args_parameters[command_manager.command])
    assert command_details == {
        'input': 'test.rss',
        'output': 'test.json',
        'sort': 'asc',
        'author': 'first_name second_name last_name',
        'limit': '1'
    }


def test_initialize_args_with_incorrect_arg(command_line_with_mistake, command_args_parameters):
    """Test transform options to dict method failure in case of incorrect input."""

    command_manager = CommandManager(command_line_with_mistake[1], command_line_with_mistake[2:])
    with pytest.raises(OptionFormatException):
        command_details = command_manager.initialize_args(command_args_parameters[command_manager.command])
