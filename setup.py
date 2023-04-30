from setuptools import find_packages, setup

setup(
      name='musique',
      version='0.0.1',
      description='Create lists of Spotify lists using ChatGPT.',
      long_description=open('README.rst').read(),
      author="Gaston L'Huillier",
      author_email='glhuilli@gmail.com',
      license='Apache 2',
      packages=find_packages(),
      package_data={
            '': ['README.rst', 'LICENSE']
      },
      zip_safe=False,
      install_requires=[x.strip() for x in open("requirements.txt").readlines()])