import unittest
import tempfile
import shutil
from pathlib import Path

from python_preprocessor.preprocess_folder import folder_to_processing_units
from python_preprocessor.define.processing_unit import ProcessingUnit

class TestFolderToProcessingUnits(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = Path(tempfile.mkdtemp())

        # Create a sample directory structure
        (self.test_dir / "subfolder1").mkdir()
        (self.test_dir / "subfolder2").mkdir()

        # Create some sample files
        (self.test_dir / "file1.py").touch()
        (self.test_dir / "file2.txt").touch() # not .py file
        (self.test_dir / "subfolder1" / "file3.py").touch()
        (self.test_dir / "subfolder2" / "file4.py").touch()

    def tearDown(self):
        # Remove the temporary directory after the test
        shutil.rmtree(self.test_dir)

    def test_preprocess_folder(self):
        # Run the preprocess_folder function
        processing_units = folder_to_processing_units(self.test_dir)

        # Check if the correct number of ProcessingUnit objects were created
        self.assertEqual(len(processing_units), 3)

        # Check if all ProcessingUnit objects are for .py files
        for unit in processing_units:
            self.assertIsInstance(unit, ProcessingUnit)
            self.assertEqual(unit.file.suffix, '.py')

        # Check if the correct files were processed
        processed_files = set(unit.file.name for unit in processing_units)
        expected_files = {'file1.py', 'file3.py', 'file4.py'}
        self.assertEqual(processed_files, expected_files)

if __name__ == '__main__':
    unittest.main()