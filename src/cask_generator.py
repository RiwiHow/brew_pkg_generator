from pathlib import Path

from constant import CASK_TEMPLATE, NO_QUARANTINE_TEMPLATE
from json_reader import json_reader


def _cask_generator(file):
    cask_output_path, quarantineStatus, name, version, asset_name, sha256, url = (
        json_reader(file)
    )

    staged_file_path = f"#{'{staged_path}'}/{asset_name}/{name}"
    noQuarantine = (
        NO_QUARANTINE_TEMPLATE.format(staged_file_path=staged_file_path)
        if quarantineStatus
        else ""
    )

    cask = CASK_TEMPLATE.format(
        name=name,
        version=version,
        sha256=sha256,
        url=url,
        asset_name=asset_name,
        noQuarantine=noQuarantine,
    ).lstrip()
    Path(cask_output_path).mkdir(exist_ok=True, parents=True)

    with open(f"{cask_output_path}/{name}.rb", "w") as f:
        f.write(cask)


def generator_from_url():
    _cask_generator(False)


def generator_from_file():
    _cask_generator(True)
