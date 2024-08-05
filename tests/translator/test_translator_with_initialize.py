import glob

import pytest

from localtrans.models.exceptions import PytFolderNotFoundError
from localtrans.translator import Translate
from pathlib import Path


class TestTranslatorWithInitialize:
    def test_translator_with_initialize(self, PYTValidFilesPathFactory):
        files_path = PYTValidFilesPathFactory

        test_files = glob.glob(f'{files_path}/*.pyt')
        lang_names = [Path(file).stem for file in test_files]

        translator = Translate.initialize(files_path)

        assert len(translator.lang_names) == len(lang_names)
        assert sorted(lang_names) == sorted(translator.lang_names)

    def test_translator_with_initialize_if_folder_not_exist(self):
        files_path = './there_is_no_folder_with_this_name'

        with pytest.raises(PytFolderNotFoundError):
            Translate.initialize(files_path)
