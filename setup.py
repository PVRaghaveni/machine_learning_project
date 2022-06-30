from setuptools import setup, find_packages
from typing import List



# Declaring variables for setup function
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.4"
AUTHOR = "Raghaveni"
DESCRIPTION = "This is my FSDS Machine Learning Project"
PACKAGES = ["housing"]
REQUIREMENTS_FILE_NAME = "requirements.txt"

def get_requirements_list() ->List[str]:    

    """
    Description : This function is going to return list of requirements mention in requirements.txt file.

    return This function is going to return list of requirements mention in requirements.txt file.
    """
    with open(REQUIREMENTS_FILE_NAME) as reuirement_file:
        return reuirement_file.readlines().remove("-e .")


setup(name = PROJECT_NAME,
version = VERSION,
author = AUTHOR,
description = DESCRIPTION,
packages = find_packages(),
install_requires = get_requirements_list()
)
