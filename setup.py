from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e.'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        # reading everthing from req file
        requirements=file_obj.readlines()
        #repalcinf the \n from the files and making a list
        requirements=[req.replace("\n","") for req in requirements]
        # removing -e . from the requirements if present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='MLProject',
    version='0.0.1',
    author='Jimpi',
    author_email='jimpidesk@gmail.com',
    description='A machine learning project template',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)