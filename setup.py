import io
import os.path as path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

requirements_path = path.join(here, "requirements", "prod.txt")

readme_path = path.join(here, "README.md")


def read_requirements(path):
    try:
        with io.open(path, mode="rt", encoding="utf-8") as fp:
            return list(
                filter(bool, [line.split("#")[0].strip() for line in fp])  # noqa:C407
            )
    except IndexError:
        raise RuntimeError("{} is broken".format(path))


def read_readme(path):
    with io.open(path, mode="rt", encoding="utf-8") as fp:
        return fp.read()


setup(
    name="python-lei",
    description="Python wraper for Legal Entity Identification API and ISIN to LEI and vice versa conversion.",
    version="0.1",
    long_description=read_readme(readme_path),
    long_description_content_type="text/markdown",
    setup_requires=["setuptools_scm"],
    install_requires=read_requirements(requirements_path),
    include_package_data=True,
    package_data={},
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    author="jdvala",
    author_email="jay.vala@msn.com",
    url="https://github.com/jdvala/python-lei",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    keywords="LEI python-lei Legal Entity Identification ISIN Finance",
    license="MIT",
)
