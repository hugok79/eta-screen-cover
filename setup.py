#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

APP_NAME = "eta-screen-cover"
APP_ID = "tr.org.pardus.eta-screen-cover"

data_files = [
    # Sources
    (
        f"/usr/share/pardus/{APP_NAME}/src",
        ["src/Main.py", "src/MainWindow.py"],
    ),
    # Data
    (f"/usr/share/pardus/{APP_NAME}/data", ["data/style.css"]),
    # Executable
    ("/usr/bin/", [f"{APP_NAME}"]),
    # Icon
    (f"/usr/share/pardus/{APP_NAME}/", [f"{APP_NAME}.svg"]),
    ("/usr/share/icons/hicolor/scalable/apps/", [f"{APP_NAME}.svg"]),
    # Desktop
    ("/usr/share/applications/", [f"{APP_ID}.desktop"]),
]

setup(
    name=f"{APP_NAME}",
    version="0.1.0",
    packages=find_packages(),
    scripts=[f"{APP_NAME}"],
    install_requires=["PyGObject"],
    data_files=data_files,
    author="Emin Fedar",
    author_email="emin.fedar@pardus.org.tr",
    description="Screen cover app for ETA",
    license="GPLv3",
    keywords="",
    url="https://github.com/pardus/eta-screen-cover",
)
