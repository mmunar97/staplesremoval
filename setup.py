from setuptools import setup

setup(
    name='staplesremoval',
    version='1.2',
    packages=['staplesremoval'],
    url='https://github.com/mmunar97',
    license='mit',
    author='marcmunar',
    author_email='marc.munar1@estudiant.uib.es',
    description='Algorithm for staple detection and mask generation',
    install_requires = [
        'matplotlib',
        'scipy',
        'scikit-image',
        'softcolor'
    ]
)
