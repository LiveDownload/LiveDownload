import sys
from setuptools import setup, find_packages

install_requires = [
    'Click>=7.0',
    'aiohttp>=3.6.2, <4.0',
    'colorlog>=4.1.0',
]

if sys.version_info < (3, 7):
    install_requires.append('dataclasses>=0.7')

setup(
    name='livedownload',
    keywords=['LiveDownload', 'bilibili'],
    license='GNU General Public License v3',
    description='',
    version='1.0.1',
    packages=find_packages(),
    url='https://github.com/LiveDownload/LiveDownload',
    python_requires='>=3.6',
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'livedownload=livedownload.main:main',
        ],
    },
    zip_safe=False
)