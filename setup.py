from setuptools import find_packages, setup

setup(
    name="kaggle_data_cleaning",
    packages=find_packages(exclude=["kaggle_data_cleaning_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "kaggle",
        "pandas",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
) 