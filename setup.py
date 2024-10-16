# NOTE: This setup.py file is kept for reference purposes only.
# This project is managed using Poetry. Please refer to pyproject.toml
# for the current project configuration and dependencies.

from setuptools import setup, find_packages

setup(
    name="morning_greetings",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
       "python-dotenv",
       "schedule",
       "logging"
       "datetime",
       "csv",
       "pytz",
       "os",
       "sys",
       "typing",
       "dataclasses",
       "logging",
       "time"
    ],
    author="Ruby Jane Cabagnot",
    author_email="rucab3109@oslomet.no",
    description="A package for generating and sending morning greetings",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rubyjane88/morning_greetings",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "morning_greetings=morning_greetings.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "morning_greetings": ["data/*.txt"],
    },
)   
