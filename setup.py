from setuptools import setup

setup(name='pd2gs',
      version='0.1',
      description='Simple tool to export pandas dataframes to google sheets.',
      url='https://github.com/Ozzerov/pd2gs',
      author='Alex Ozerov & Roman Solovev',
      author_email='ozerov@yandex.ru',
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: All who use python for data analysis',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
      ],
      keywords='pandas googlesheet',
      packages=['pd2gs'],
      install_requires=['gspread', 'oauth2client'],
      zip_safe=False)
