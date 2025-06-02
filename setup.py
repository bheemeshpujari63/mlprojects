from setuptools import setup, find_packages

def get_requirements(file_path):
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]
    return [req for req in requirements if req != '-e .']

setup(
    name='mlproject',
    version='0.0.1',
    author='Bheemesh',
    author_email='bheemeshpujari63@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=get_requirements("requirements.txt"),
)
