import pytest

from localtrans.models.exceptions import NoTranslationError, LanguageNameExistError, FileFormatValidationError
from localtrans.translator import Translate
import random


class TestTranslate:
    def test_translate(self, PYTValidFilesPathWithWordsFactory):
        path, keys = PYTValidFilesPathWithWordsFactory

        translator = Translate.initialize(path)

        selected_lang = random.choice(list(keys.keys()))
        selected_word = random.choice(list(keys[selected_lang].keys()))
        translated = translator.translate(selected_lang, selected_word)

        assert translated == keys[selected_lang][selected_word]

    def test_translate_if_word_not_exist(self, PYTValidFilesPathWithWordsFactory):
        path, keys = PYTValidFilesPathWithWordsFactory

        translator = Translate.initialize(path)

        selected_lang = random.choice(list(keys.keys()))
        selected_word = 'not-exist-word'

        with pytest.raises(NoTranslationError):
            translator.translate(selected_lang, selected_word)

    def test_translate_if_word_not_exist_but_raise_error_false(self, PYTValidFilesPathWithWordsFactory):
        path, keys = PYTValidFilesPathWithWordsFactory

        translator = Translate.initialize(path, raise_error=False)

        selected_lang = random.choice(list(keys.keys()))
        selected_word = 'not-exist-word'

        translated = translator.translate(selected_lang, selected_word)

        assert not translated

    def test_translate_if_file_has_same_keys(self, PYTSameKeysFilesPathWithWordsFactory):
        path, keys = PYTSameKeysFilesPathWithWordsFactory

        translator = Translate.initialize(path)

        selected_lang = random.choice(list(keys.keys()))
        selected_word = random.choice(list(keys[selected_lang].keys()))

        with pytest.raises(FileFormatValidationError):
            translator.translate(selected_lang, selected_word)
