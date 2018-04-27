from __future__ import print_function

import sys
import os.path
from setuptools import setup, find_packages
from setuptools.command.install import install
from distutils.core import Command
import io
PTH = 'pypy-fix-cython-warning.pth'

class install_with_pth(install):
    sub_commands = install.sub_commands + [
        ('install_pth_hack', lambda self:
            self.single_version_externally_managed)
    ]

class install_pth_hack(Command):
    user_options = [
        ('install-dir=', 'd', "directory to install to"),
    ]

    @property
    def target(self):
        return os.path.join(self.install_dir, PTH)

    def get_outputs(self):
        return [self.target]

    def initialize_options(self):
        self.install_dir = None

    def finalize_options(self):
        self.set_undefined_options(
            'install', ('install_lib', 'install_dir'))

    def run(self):
        with open(PTH) as infp:
            with open(self.target, 'w') as outfp:
                outfp.write(infp.read())


setup(
    name='pypy_fix_cython_warning',
    use_scm_version=True,
    author='Antonio Cuni',
    author_email='anto.cuni@gmail.com',
    py_modules=[],
    url='http://github.com/antocuni/pypy-fix-cython-warning',
    license='MIT',
    description='Ignore the spurious and annoying Cython warnings in PyPy 6.0',
    keywords='pypy cython',
    setup_requires=['setuptools_scm'],
    cmdclass={
        'install': install_with_pth,
        'install_pth_hack': install_pth_hack,
    }
)
