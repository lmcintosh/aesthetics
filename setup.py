from setuptools import setup

setup(name = 'aesthetics',
        version = '0.1',
        description = 'A library with often-called functions for making matplotlib plots pretty',
        author = 'Lane McIntosh',
        author_email = 'lmcintosh@stanford.edu',
        url = 'https://github.com/lmcintosh/aesthetics.git',
        long_description = '''
            Aesthetics functions for python's matplotlib library.
            ''',
        classifiers = [
            'Intended Audience :: Science/Research',
            'Operating System :: MacOS :: MacOS X',
            'Topic :: Utilities'],
        packages = ['aesthetics'],
        package_dir = {'aesthetics': 'aesthetics/'},
        py_modules = ['aesthetics']
        )
