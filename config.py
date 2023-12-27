from file_converter.commands.converter_command import ConverterCommand

command_config = {
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
