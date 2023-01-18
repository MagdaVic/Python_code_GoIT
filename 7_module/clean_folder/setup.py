from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='Sorting files into folders accoding to their extentions',
    url='https://github.com/MagdaVic/Tutorial',
    author='MagdaVic',
    author_email='',
    license='MIT',
    packages=find_namespace_packages(),
    # install_requires=['',''], if needs to install some else packadges before installing clean_folder
    entry_points={'console_scripts': ['clean-folder=clean_folder.clean:main']}
    )