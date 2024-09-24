import argparse
from pathlib import Path
import shutil
import sys

from python_preprocessor.preprocess_folder import preprocess_folder


def main():
    parser = argparse.ArgumentParser(description="Python Preprocessor")
    parser.add_argument("input_folder", type=Path, help="Path to the input folder")
    parser.add_argument("output_folder", type=Path, help="Path to the output folder")
    args = parser.parse_args()

    input_folder = args.input_folder
    output_folder = args.output_folder

    print(f"Input folder:  {input_folder}")
    print(f"Output folder: {output_folder}")

    if not input_folder.is_dir():
        print(
            f"Error: Input folder '{input_folder}' does not exist or is not a directory."
        )
        sys.exit(1)

    shutil.copytree(input_folder, output_folder, dirs_exist_ok=True)

    try:
        shutil.copytree(input_folder, output_folder, dirs_exist_ok=True)
    except Exception as e:
        sys.exit(1)

    preprocess_folder(output_folder)


if __name__ == "__main__":
    main()
