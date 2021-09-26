import glob
from pathlib import Path
from typing import Iterator, List

from setuptools import find_namespace_packages, setup


DESCRIPTION = "A fully type-annotated Rust-like Result type for Python."


def long_description() -> str:
    return Path("README.md").read_text()


def install_requires() -> List[str]:
    return list(_requires("requirements.in"))


def tests_require() -> List[str]:
    return list(_requires("requirements-dev.in"))


def _requires(reqtxt_basename: str) -> Iterator[str]:
    reqtxt = Path(__file__).parent / reqtxt_basename
    reqs = reqtxt.read_text().split("\n")
    for req in reqs:
        if not req or req.lstrip().startswith(("#", "-")):
            continue
        yield req


setup(
    author="Bryan M Bugyi",
    author_email="bryanbugyi34@gmail.com",
    python_requires=">=3.7",
    install_requires=install_requires(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description=DESCRIPTION,
    entry_points={
        "console_scripts": [
            "result = result.cli:main",
        ]
    },
    scripts=glob.glob("scripts/*"),
    license="MIT license",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    name="python-result",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    test_suite="tests",
    tests_require=tests_require(),
    url="https://github.com/bbugyi200/result",
    use_scm_version={"fallback_version": "0.0.1"},
    zip_safe=False,
)
