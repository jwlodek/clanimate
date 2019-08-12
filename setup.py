import setuptools

with open('README.md', 'r') as readme_fp:
    long_description = readme_fp.read()


setuptools.setup(
    name='clanimate',
    description='A CLI loading bar and animation python library.',
    version='0.0.1',
    author='Jakub Wlodek',
    author_email='jwlodek.dev@gmail.com',
    long_description_content_type = 'text/markdown',
    license='BSD (3-clause)',
    packages=['clanimate'],
    url='https://github.com/jwlodek/clanimate',
    python_requires='>=3.2'
)