import setuptools

with open('README.md', 'r') as readme_fp:
    long_description = readme_fp.read()


setuptools.setup(
    name='clanimate',
    version='v0.0.1',
    author='Jakub Wlodek',
    author_email='jwlodek.dev@gmail.com',
    description='A CLI loading bar and animation python library.',
    long_description_content_type = 'text/markdown',
    url='https://github.com/jwlodek/clanimate'
)