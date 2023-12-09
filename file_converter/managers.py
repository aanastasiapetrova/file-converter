from file_converter.exceptions import OptionFormatException, OptionIsRequiredException

class CommandManager:
    def __init__(self, command, args):
        self.command = command
        self.args = args


    def initialize_args(self, command_args_parameters):
        """Transform inputed command options from string to dictionary."""

        for arg in self.args:
            if arg.split('=')[0].startswith('--'):
                option = arg.split('=')[0].replace('--', '')
                command_args_parameters[option] = arg.split('=')[1]
            else:
                raise OptionFormatException(f"Command option should start with --, but option {arg.split('=')[0]} does not.")
        return command_args_parameters
    

    def get_command(self, config, initial_args):
        """Choose the correct command from config."""

        return config[self.command](*list(initial_args.values()))
