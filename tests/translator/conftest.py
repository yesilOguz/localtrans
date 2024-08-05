import os

import pytest
from faker import Faker

from pathlib import Path

Faker.seed(3)
faker = Faker()


@pytest.fixture()
def PYTValidFilesPathWithWordsFactory():
    basedir_name = './pyts'
    os.mkdir(basedir_name)
    file_paths = [f'{basedir_name}/en.pyt', f'{basedir_name}/fr.pyt', f'{basedir_name}/tr.pyt']

    dictionary = {}

    for file_path in file_paths:
        lines = ''
        translates = {}

        lang_name = Path(file_path).stem

        for _ in range(10):
            key = faker.word()
            translated = faker.word()

            if key in translates.keys():
                continue

            translates[key] = translated

            line = f'{key}={translated}\n'
            lines += line

        with open(file_path, 'w') as f:
            f.writelines(lines)

        dictionary[lang_name] = translates

    yield basedir_name, dictionary

    for file_path in file_paths:
        if not os.path.exists(file_path):
            continue
        os.remove(file_path)

    os.removedirs(basedir_name)


@pytest.fixture()
def PYTInvalidFilesPathWithWordsFactory():
    basedir_name = './pyts'
    os.mkdir(basedir_name)
    file_paths = [f'{basedir_name}/en.pyt', f'{basedir_name}/fr.pyt', f'{basedir_name}/tr.pyt']

    dictionary = {}

    for file_path in file_paths:
        lines = ''
        translates = {}

        lang_name = Path(file_path).stem

        for _ in range(10):
            key = faker.word()
            translated = faker.word()

            translates[key] = translated

            line = f'{key}{translated}\n'
            lines += line

        with open(file_path, 'w') as f:
            f.writelines(lines)

        dictionary[lang_name] = translates

    yield basedir_name, dictionary

    for file_path in file_paths:
        if not os.path.exists(file_path):
            continue
        os.remove(file_path)

    os.removedirs(basedir_name)


@pytest.fixture()
def PYTSameKeysFilesPathWithWordsFactory():
    basedir_name = './pyts'
    os.mkdir(basedir_name)
    file_paths = [f'{basedir_name}/en.pyt', f'{basedir_name}/fr.pyt', f'{basedir_name}/tr.pyt']

    dictionary = {}

    for file_path in file_paths:
        lines = ''
        translates = {}

        lang_name = Path(file_path).stem

        key = faker.word()
        translated = faker.word()
        for _ in range(10):
            translates[key] = translated

            line = f'{key}{translated}\n'
            lines += line

        with open(file_path, 'w') as f:
            f.writelines(lines)

        dictionary[lang_name] = translates

    yield basedir_name, dictionary

    for file_path in file_paths:
        if not os.path.exists(file_path):
            continue
        os.remove(file_path)

    os.removedirs(basedir_name)