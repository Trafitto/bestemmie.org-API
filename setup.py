from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='bestemmie',
      version='0.2',
      description='Bestemmie.org api',
	  long_description=readme(),
	  keywords='bestemmie api bestemmie.org',
      url='https://github.com/Trafitto/bestemmie.org-API',
      author='Trafitto',
      author_email='develops@trafitto.com',
      license='MIT',
      packages=['bestemmie'],
      zip_safe=False)