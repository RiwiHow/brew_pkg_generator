from pathlib import Path

from constant import CASK_TEMPLATE
from json_reader import json_reader


def _cask_generator(file):
    cask_output_path, name, version, sha256, url = json_reader(file)

    cask = CASK_TEMPLATE.format(
        name=name, version=version, sha256=sha256, url=url
    ).lstrip()
    Path(cask_output_path).mkdir(exist_ok=True, parents=True)

    with open(f"{cask_output_path}/{name}.rb", "w") as f:
        f.write(cask)


def generator_from_url():
    _cask_generator(False)


def generator_from_file():
    _cask_generator(True)
