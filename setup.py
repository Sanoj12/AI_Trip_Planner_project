###local package install in the  current virual envirnoment l


from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """

    requirement_list:List[str] = []
    
    try:
        # Open and read the requirements.txt file
        with open('requirements.txt', 'r') as file:

            # Read lines from the file
            lines = file.readlines()

            # Process each line
            for line in lines:
                # Strip whitespace and newline character
                # s
                requirement = line.strip()
                # Ignore empty lines and -e .

                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found.")

    
        
    return requirement_list

print(get_requirements())

setup(
    name="AI-TRAVEL-PLANNER",
    version="3.10.18",
    author="sanoj c sam",
    author_email="sanojcsam123@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements()
)