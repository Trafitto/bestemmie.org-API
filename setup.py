from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='bestemmie',
      version='0.1',
      description='Bestemmie.org api',
	  long_description=readme(),
	  keywords='bestemmie api bestemmie.org',
      url='',
      author='Trafitto',
      author_email='develops@trafitto.com',
      license='MIT',
      packages=['bestemmie'],
	   install_requires=[
          'json',
		  'urllib',
      ],
      zip_safe=False)