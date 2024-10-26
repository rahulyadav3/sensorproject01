# yeh package h jo tools provide krta hai packaging kr liye python projects
# find packages project k andr packagee find krta hai
from setuptools import find_packages,setup
# project k package ka details sara iss file mei mentioned hai
from typing import List
HYPEN_E_DOT='-e.'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='Fault detection',
    # version='0.0.1',
    author='imran',
    author_email='md.a@pw.live',
    install_requirements=('requirements.txt'),
    packages=find_packages(),

)