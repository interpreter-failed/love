# -*- coding: utf-8 -*-

from importlib.resources import Package
import setuptools as st


PACKAGE_NAME = "love"

st.setup(
    name=PACKAGE_NAME,
    version="0.3.0",
    package_dir={'': 'src'},
    packages=st.find_packages(exclude=["letters"]),
    install_requires=[
        "cryptography"
    ],
    entry_points={
        "console_scripts": [
            f"{PACKAGE_NAME}.letters={PACKAGE_NAME}.__init__:letters_main",
            f"{PACKAGE_NAME}.meeting={PACKAGE_NAME}.__init__:meeting_main",
        ]
    },
    zip_safe=False,
)
