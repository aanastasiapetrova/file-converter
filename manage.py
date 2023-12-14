import sys

from file_converter.commands import ConverterCommand
from file_converter.managers import CommandManager

config = {
    "converter": ConverterCommand,
}

command_args_parameters = {
    "converter": {
        "input": None,
        "output": None,
        "sort": None,
        "author": None,
        "limit": None,
    },
}


if __name__ == "__main__":
    command_manager = CommandManager(sys.argv[1], sys.argv[2:])

    command_details = command_manager.initialize_args(
        command_args_parameters[command_manager.command]
    )
    command = command_manager.get_command(config, command_details)

    print(command.info())
    command.start()
