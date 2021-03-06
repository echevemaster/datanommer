from setuptools import setup, find_packages
import sys

f = open('README.rst')
long_description = f.read().strip()
long_description = long_description.split('split here', 1)[1]
f.close()

version = '0.4.5'

setup(
    name='datanommer.commands',
    version=version,
    description="Console comands for datanommer",
    long_description=long_description,
    author='Ralph Bean',
    author_email='rbean@redhat.com',
    url='http://github.com/fedora-infra/datanommer',
    license='GPLv3+',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['datanommer'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "datanommer.models",
        "fedmsg",
    ],
    entry_points={
        'console_scripts': (
            'datanommer-create-db=datanommer.commands:create',
            'datanommer-dump=datanommer.commands:dump',
            'datanommer-stats=datanommer.commands:stats',
            'datanommer-latest=datanommer.commands:latest',
        ),
    },
)
