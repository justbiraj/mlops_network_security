from setuptools import find_packages, setup
from typing import List

def get_requirement()->List[str]:
    requirements = []
    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()
                if requirement and requirement!= '-e .':
                    requirements.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found. No dependencies will be installed.")
            
    return requirements

# print(get_requirement())

setup(
    name="network_security",
    version="0.0.1",
    author="Biraj Mishra",
    packages=find_packages(),
    install_requires=get_requirement(),
)