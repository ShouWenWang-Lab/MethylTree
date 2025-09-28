import os
import sys
from pathlib import Path

from setuptools import find_packages, setup

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

setup(
    name="methyltree",  # this name does not matter, what matter is the folder name that contains the __init__.py
    version="1.0.0",
    python_requires=">=3.9",
    packages=["methyltree"],  # Include only the methyltree package
    author="Shou-Wen Wang",
    author_email="wangshouwen@westlake.edu.cn",
    description="MethyTree: High-resolution, noninvasive single-cell lineage tracing based on DNA methylation epimutations",
    long_description=Path("README.md").read_text("utf-8"),
    license="License :: Other/Proprietary License",
)
