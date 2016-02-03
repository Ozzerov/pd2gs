from setuptools import setup

setup(name='pd2gs',
      version='0.1',
      description='Simple tool to export pandas dataframes to google sheets.',
      url='https://github.com/Ozzerov/pd2gs',
      author='Alex Ozerov',
      author_email='ozerov@yandex.ru',
      license='MIT',
      packages=['pd2gs'],
      install_requires=['gspread', 'oauth2client'],
      zip_safe=False)
