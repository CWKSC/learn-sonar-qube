from pathlib import Path

from python_preprocessor.define.processing_unit import ProcessingUnit


# Receive a folder path, and do the preprocessing work in place in the folder
def preprocess_folder(folder: Path):
    processing_units = folder_to_processing_units(folder)
    print(processing_units)


def folder_to_processing_units(folder: Path, pattern: str = "*.py"):
    processing_unit_list = []
    for path in folder.rglob(pattern):
        if path.is_file():
            processing_unit_list.append(ProcessingUnit(path))
    return processing_unit_list
