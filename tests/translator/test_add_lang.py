from pathlib import Path

import pytest

from localtrans.models.exceptions import LanguageNameExistError, PytFileNotFoundError
from localtrans.models.pytranslator import PytFile
from localtrans.translator import Translate


class TestAddLang:
    def test_add_lang(self, PYTValidFilesPathFactory, SingleValidPYTFilePathFactory):
        files_path = PYTValidFilesPathFactory
        single_file = SingleValidPYTFilePathFactory

        pyt_path = Path(single_file)

        lang_name = pyt_path.stem
        lang_file_path = single_file
        single_pyt_file = PytFile(language_name=lang_name, file_path=lang_file_path)

        translator = Translate.initialize(files_path)
        before_num_of_langs = len(translator.lang_names)

        assert before_num_of_langs > 0

        translator.add_lang(single_pyt_file)

        assert before_num_of_langs < len(translator.lang_names)

    def test_add_lang_if_lang_name_exist_in_object(self, PYTValidFilesPathFactory, SingleValidPYTFilePathFactory):
        files_path = PYTValidFilesPathFactory
        single_file = SingleValidPYTFilePathFactory

        translator = Translate.initialize(files_path)
        before_num_of_langs = len(translator.lang_names)

        assert before_num_of_langs > 0

        single_pyt_file = PytFile(language_name=next(iter(translator.lang_names)), file_path=single_file)

        with pytest.raises(LanguageNameExistError):
            translator.add_lang(single_pyt_file)

    def test_add_lang_if_file_not_exist(self, PYTValidFilesPathFactory):
        files_path = PYTValidFilesPathFactory
        single_file = './this_file_not_exist.pyt'

        translator = Translate.initialize(files_path)

        single_pyt_file = PytFile(language_name='not-exist', file_path=single_file)

        with pytest.raises(PytFileNotFoundError):
            translator.add_lang(single_pyt_file)
