from setuptools import setup, find_packages
from django_crm import __version__ as version


setup(
    name='Django CRM',
    version=version,
    description='Django CRM Framework',
    author='Jesus Anaya',
    author_email='jesus.anaya.dev@gmail.com',
    license="BSD",
    include_package_data=True,
    url='https://github.com/JesusAnaya/django-crm/',
    packages=find_packages(),
)
