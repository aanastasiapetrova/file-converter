import os
import sys
import importlib
import file_converter.constants as constants


class Registrator:
    
    def __init__(self, path):
        self.path = path


    def get_manager(self, manager_dir):
        cwd = os.path.abspath(os.getcwd())
        converter_dir = os.path.join(cwd, "file_converter")
        managers_dir = os.path.join(converter_dir, "managers")
        module_dir = ".".join(managers_dir.split("\\")[5:])

        manager_module = [man for man in os.listdir(managers_dir) if man.startswith(manager_dir)][0].split(".")[0]
        if manager_module not in list(sys.modules.keys()):
            globals()[manager_module] = importlib.import_module(".".join([module_dir, manager_module])).__dict__[manager_module]

        return globals()[manager_module]

    
    def register(self):
        module_dir = ".".join(self.path.split("\\")[5:])
        manager_dir = self.path.split("\\")[-1]
        manager = self.get_manager(manager_dir)

        list_dir = os.listdir(self.path)
        files_to_register = []

        for item in list_dir:
            if os.path.isfile(os.path.join(self.path, item)) and item not in constants.FILES_TO_IGNORE and not item.startswith("base"):
                files_to_register.append(item.split(".")[0])
        
        for file in files_to_register:
            module = ".".join([module_dir, file])
            global to_import
            to_import = "".join([word.capitalize() for word in file.split("_")])
                
            globals()[to_import] = importlib.import_module(module).__dict__[to_import]
            manager.register(globals()[to_import].get_format(), globals()[to_import])
        
