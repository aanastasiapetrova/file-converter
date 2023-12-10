from file_converter.exceptions import OptionFormatException, OptionIsRequiredException

class CommandManager:
    """Command manager class to manage commands classes."""
    
    def __init__(self, command, args):
        self.command = command
        self.args = args

    @staticmethod
    def is_option(option):
        count = 0

        for symb in option:
            if symb == '-':
                count += 1
            else:
                break

        match count:
            case 0:
                return False
            case 2:
                return True
            case _:
                raise OptionFormatException(f"Command option should start with --, but option {option} does not.")


    def initialize_args(self, command_args_parameters):
        """Transform inputed command options from string to dictionary."""

        offset = 1

        for i in range(len(self.args)):
            option = self.args[i].split('=')[0]
            if CommandManager.is_option(option):
                offset = 1
                option = self.args[i].split('=')[0].replace('--', '')
                command_args_parameters[option] = self.args[i].split('=')[1]
            else:
                self.args[i-offset] += ' ' + self.args[i]
                option = self.args[i-offset].split('=')[0].replace('--', '')
                command_args_parameters[option] += ' '
                command_args_parameters[option] += self.args[i].split('=')[0]
                offset += 1

        return command_args_parameters
    

    def get_command(self, config, initial_args):
        """Choose the correct command from config."""

        return config[self.command](*list(initial_args.values()))
