from constant import CASK_OUTPUT_PATH, CASK_TEMPLATE
from json_reader import json_reader


def _cask_generator(file):
    name, version, sha256, url = json_reader(file)

    cask = CASK_TEMPLATE.format(
        name=name, version=version, sha256=sha256, url=url
    ).lstrip()

    with open(f"{CASK_OUTPUT_PATH}/{name}.rb", "w") as f:
        f.write(cask)


def generator_from_url():
    _cask_generator(False)


def generator_from_file():
    _cask_generator(True)
