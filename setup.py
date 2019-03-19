from setuptools import setup, find_packages

setup(
    name='package_function',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/neomopedi/package_function.git',
    author='<Neo Mopedi>',
    author_email='<neo.mopedi@gmail.com>'
)
