from setuptools import setup, find_packages

try:
    with open("README.md", "r") as f:
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
    install_requires=[
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "nixos-wizard-rebuild=wizard.__main__:rebuild",
            "nixos-wizard-cleanup=wizard.__main__:cleanup",
            "nixos-wizard-update=wizard.__main__:update",
        ]
    }
)
