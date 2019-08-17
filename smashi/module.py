import importlib.util
import os

def from_path(path):
    module_name,file_ext = os.path.splitext(os.path.split(path)[-1])

    module_spec = importlib.util.spec_from_file_location(
        module_name, path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module
