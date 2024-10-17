#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess

from setuptools import setup, find_packages

APP_NAME = "eta-screen-cover"
APP_ID = "tr.org.pardus.eta-screen-cover"


def create_mo_files():
    podir = "po"
    mo = []
    for po in os.listdir(podir):
        if po.endswith(".po"):
            os.makedirs("{}/{}/LC_MESSAGES".format(podir, po.split(".po")[0]), exist_ok=True)
            mo_file = "{}/{}/LC_MESSAGES/{}".format(podir, po.split(".po")[0], "{}.mo".format(APP_NAME))
            msgfmt_cmd = 'msgfmt {} -o {}'.format(podir + "/" + po, mo_file)
            subprocess.call(msgfmt_cmd, shell=True)
            mo.append(("/usr/share/locale/" + po.split(".po")[0] + "/LC_MESSAGES",
                       ["po/" + po.split(".po")[0] + "/LC_MESSAGES/{}.mo".format(APP_NAME)]))
    return mo


data_files = [
                 # Sources
                 (f"/usr/share/pardus/{APP_NAME}/src",
                  ["src/Main.py",
                   "src/MainWindow.py"]),
                 # Data
                 (f"/usr/share/pardus/{APP_NAME}/data",
                  ["data/style.css"]),
                 # Executable
                 ("/usr/bin/",
                  [f"{APP_NAME}"]),
                 # Icon
                 (f"/usr/share/pardus/{APP_NAME}/",
                  [f"{APP_NAME}.svg"]),
                 ("/usr/share/icons/hicolor/scalable/apps/",
                  [f"{APP_NAME}.svg"]),
                 # Desktop
                 ("/usr/share/applications/",
                  [f"{APP_ID}.desktop"]),
             ] + create_mo_files()

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
