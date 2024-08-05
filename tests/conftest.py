import math

import pytest
from faker import Faker
import random

import os

Faker.seed(3)
faker = Faker()


@pytest.fixture()
def SingleValidPYTFilePathFactory():
    lines = ''
    file_path = 'temp.pyt'

    for _ in range(10):
        key = faker.word()
        translated = faker.word()

        line = f'{key}={translated}\n'
        lines += line

    with open(file_path, 'w') as f:
        f.writelines(lines)

    yield file_path

    os.remove(file_path)


@pytest.fixture()
def SingleValidPYTFilePathWithoutRemoveFactory():
    lines = ''
    file_path = 'temp.pyt'

    for _ in range(10):
        key = faker.word()
        translated = faker.word()

        line = f'{key}={translated}\n'
        lines += line

    with open(file_path, 'w') as f:
        f.writelines(lines)

    return file_path


@pytest.fixture()
def SingleInvalidPYTFilePathFactory():
    lines = ''
    file_path = 'temp.pyt'

    for _ in range(10):
        key = faker.word()
        translated = faker.word()
        invalid_delimiters = '!^+-?:.%&'

        selected_delimiter = invalid_delimiters[math.floor(random.random() * len(invalid_delimiters))]

        line = f'{key}{selected_delimiter}{translated}\n'
        lines += line

    with open(file_path, 'w') as f:
        f.writelines(lines)

    yield file_path

    os.remove(file_path)


@pytest.fixture()
def PYTValidFilesPathFactory():
    basedir_name = './pyts'
    os.mkdir(basedir_name)
    file_paths = [f'{basedir_name}/en.pyt', f'{basedir_name}/fr.pyt', f'{basedir_name}/tr.pyt']

    for file_path in file_paths:
        lines = ''

        for _ in range(10):
            key = faker.word()
            translated = faker.word()

            line = f'{key}={translated}\n'
            lines += line

        with open(file_path, 'w') as f:
            f.writelines(lines)

    yield basedir_name

    for file_path in file_paths:
        if not os.path.exists(file_path):
            continue
        os.remove(file_path)

    os.removedirs(basedir_name)
