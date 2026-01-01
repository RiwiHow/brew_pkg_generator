import json
from pathlib import Path

import requests

from constant import JSON_PATH, RELEASE_API, Cask


def json_reader(file: bool):
    with open(JSON_PATH, "r") as f:
        cask: Cask = json.load(f)

    if not file:
        url_parts = "/".join(cask["url"].split("/")[3:5])
        release_url = RELEASE_API + f"{url_parts}/releases"

        response = requests.get(release_url)
        if response.status_code == 200:
            release_json = response.json()
        else:
            raise RuntimeError("Unable to fetch releases")
    else:
        temp_json_path = Path(__file__).resolve().parents[1] / "releases.json"
        with open(temp_json_path, "r") as f:
            release_json = json.load(f)

    if cask["preRelease"] == 1:
        release = next((item for item in release_json if item["prerelease"] == 1))
    else:
        release = next((item for item in release_json if item["prerelease"] == 0))

    version = release["name"]
    target_asset = next(
        item for item in release["assets"] if "darwin-arm64.tar.gz" in item["name"]
    )
    sha256 = target_asset["digest"].split("sha256:")[1]
    download_url = target_asset["browser_download_url"]

    return cask["name"], version, sha256, download_url
