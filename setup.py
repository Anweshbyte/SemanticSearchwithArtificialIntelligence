from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(path:str)->List[str]:
    req=[]
    with open(path) as file:
        req=file.readline()
        req=[requ.replace("\n","") for requ in req]

        if HYPHEN_E_DOT in req:
            req.remove(HYPHEN_E_DOT)

    return req

setup(
    name="Semantic-Seach-Using-AI",
    version='0.0.1',
    author='Arindom Bora',
    author_email='arindombora10@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
