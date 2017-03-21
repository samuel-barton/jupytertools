
from distutils.core import setup

setup(name='jupytertools',
      version='1.141',
      description='Tools for Scientific Programming with Jupyter Notebooks',
      author='Samuel Barton',
      author_email='samwisebarton@gmail.com',
      url='https://github.com/samuel-barton/jupytertools',
      packages=['jupytertools','jupytertools.plotting'],
      install_requires=['matplotlib'],
     )
