from pathlib import Path
from typing import TypedDict

JSON_PATH = Path(__file__).resolve().parents[1] / "cask.json"
RELEASE_API = "https://api.github.com/repos/"


class Cask(TypedDict):
    name: str
    url: str
    preRelease: int
    caskPath: str
    quarantineStatus: int


CASK_TEMPLATE = """
cask "{name}" do
    version "{version}"
    sha256 "{sha256}"
    url "{url}"

    binary "{asset_name}/{name}"

    {noQuarantine}
end
"""

NO_QUARANTINE_TEMPLATE = """
    postflight do
        system "xattr", "-d", "com.apple.quarantine", "{staged_file_path}"
    end
"""
