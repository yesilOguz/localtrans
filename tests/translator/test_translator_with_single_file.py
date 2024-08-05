from pathlib import Path

import pytest

from localtrans.models.exceptions import LanguageNameExistError, PytFileNotFoundError
from localtrans.translator import Translate
from localtrans.models.pytranslator import PytFile


class TestTranslatorWithSingleFile:
    def test_translator_with_single_file(self, SingleValidPYTFilePathFactory):
        single_file_path = SingleValidPYTFilePathFactory

        pyt_path = Path(single_file_path)

        lang_name = pyt_path.stem
        lang_file_path = single_file_path

        single_pyt_file = PytFile(language_name=lang_name, file_path=lang_file_path)

        translator = Translate(pyt_files=[single_pyt_file])

        assert len(translator.lang_names) == 1

    def test_translator_with_single_file_if_two_lang_has_same_name(self, SingleValidPYTFilePathFactory):
        single_file_path = SingleValidPYTFilePathFactory

        pyt_path = Path(single_file_path)

        lang_name = pyt_path.stem
        lang_file_path = single_file_path

        single_pyt_file = PytFile(language_name=lang_name, file_path=lang_file_path)

        with pytest.raises(LanguageNameExistError):
            Translate(pyt_files=[single_pyt_file, single_pyt_file])

    def test_translator_with_single_file_if_pyt_file_not_exist(self):
        single_file_path = './this_file_not_exist.pyt'

        pyt_path = Path(single_file_path)

        lang_name = pyt_path.stem
        lang_file_path = single_file_path

        single_pyt_file = PytFile(language_name=lang_name, file_path=lang_file_path)

        with pytest.raises(PytFileNotFoundError):
            Translate(pyt_files=[single_pyt_file])
