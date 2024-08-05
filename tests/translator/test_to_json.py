import random

from localtrans.translator import Translate


class TestToJson:
    def test_to_json(self, PYTValidFilesPathWithWordsFactory):
        path, keys = PYTValidFilesPathWithWordsFactory

        translator = Translate.initialize(path)

        selected_lang = random.choice(list(keys.keys()))
        selected_word = random.choice(list(keys[selected_lang].keys()))
        json_translator = translator.to_json(lang=selected_lang)

        translated = json_translator[selected_word]

        assert translated == keys[selected_lang][selected_word]
