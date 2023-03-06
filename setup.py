from setuptools import setup

VERSION = '0.99'

if __name__ == '__main__':
    setup(
        name='okabeito',
        packages=['okabeito'],
        version=VERSION,
        description='Okabe-Ito color palette',
        author='Jim Rybarski',
        author_email='jim@rybarski.com',
        url='https://github.com/jimrybarski/okabe-ito-py',
        download_url='https://github.com/jimrybarski/okabe-ito-py/tarball/%s' % VERSION,
        keywords=['visualization', 'color', 'palette', 'okabe', 'ito'],
        classifiers=['Development Status :: 5 - Production/Stable', 'License :: Freely Distributable', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3']
    )
