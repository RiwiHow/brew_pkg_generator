from pathlib import Path
from typing import TypedDict

JSON_PATH = Path(__file__).resolve().parents[1] / "cask.json"
RELEASE_API = "https://api.github.com/repos/"


class Cask(TypedDict):
    name: str
    url: str
    preRelease: int
    caskPath: str


CASK_TEMPLATE = """
cask "{name}" do
    version "{version}"
    sha256 "{sha256}"
    url "{url}"

    binary "sing-box-{version}-darwin-arm64/{name}"
end
"""
