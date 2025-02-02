from setuptools import setup, find_packages
from pathlib import Path

REPO_DIR = Path.cwd()

try:
    with open(REPO_DIR / "README.md", "r") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ""

setup(
    name="nixos-wizard",
    version="0.1.0",
    license="MIT",
    packages=find_packages(),
    description="simple nixos-wizard",
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        "rich",
        "pyyaml"
    ],
    entry_points={
        "console_scripts": [
            "nixos-wizard-rebuild=wizard.__main__:rebuild",
            "nixos-wizard-cleanup=wizard.__main__:cleanup",
            "nixos-wizard-update=wizard.__main__:update",
        ]
    }
)
