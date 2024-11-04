from setuptools import setup, find_packages

setup(
  name='mlops-fastapi',
  version='0.1.0',
  packages=find_packages(),
  py_modules=['main', 'app'],
  install_requires=[
    'fastapi',
    'uvicorn',
    'click'
    # Add other dependencies here
  ],
  # entry_points={
  #   'console_scripts': [
  #     'cli=cli.main:cli',  # Adjust 'main:main' to the appropriate entry point
  #     'api=main:main'
  #   ],
  # },
)