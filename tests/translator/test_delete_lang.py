import pytest

from localtrans.models.exceptions import LanguageNotExistError
from localtrans.translator import Translate
import os


class TestDeleteLang:
    def test_delete_lang(self, PYTValidFilesPathFactory):
        files_path = PYTValidFilesPathFactory

        translator = Translate.initialize(files_path)
        before_num_of_langs = len(translator.lang_names)

        selected_lang = next(iter(translator.lang_names))
        translator.delete_lang(selected_lang)

        assert os.path.exists(f'{files_path}/{selected_lang}.pyt')
        assert before_num_of_langs > len(translator.lang_names)

    def test_delete_lang_if_lang_not_exist(self, PYTValidFilesPathFactory):
        files_path = PYTValidFilesPathFactory

        translator = Translate.initialize(files_path)

        with pytest.raises(LanguageNotExistError):
            translator.delete_lang('not-exist')

    def test_delete_lang_with_file(self, PYTValidFilesPathFactory):
        files_path = PYTValidFilesPathFactory

        translator = Translate.initialize(files_path)
        before_num_of_langs = len(translator.lang_names)

        selected_lang = next(iter(translator.lang_names))
        translator.delete_lang_with_file(selected_lang)

        assert not os.path.exists(f'{files_path}/{selected_lang}.pyt')
        assert before_num_of_langs > len(translator.lang_names)

    def test_delete_lang_with_file_if_lang_not_exist(self, PYTValidFilesPathFactory):
        files_path = PYTValidFilesPathFactory

        translator = Translate.initialize(files_path)

        selected_lang = 'not-exist'

        with pytest.raises(LanguageNotExistError):
            translator.delete_lang_with_file(selected_lang)

