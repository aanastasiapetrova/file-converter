import sys

from file_converter.managers.command_manager import CommandManager
from config import command_config, command_args_parameters


def main():
    command_manager = CommandManager(sys.argv[1], sys.argv[2:])

    command_details = command_manager.initialize_args(
        command_args_parameters[command_manager.command]
    )
    command = command_manager.get_command(command_config, command_details)

    print(command.info())
    command.start()


if __name__ == "__main__":
    main()
