from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  packages = ['DSViz'],   
  name = 'DataStructureViz',       
  version = '0.0.1',      
  license='MIT',        
  description = 'DSViz is a simple and intuitive Python interface to multiple packages in order to help visualise different data structres while coding them. This package is developed mainly for students or developers who are in the process of learning data structures.',   # Give a short description about your library
  author = 'Ish Mehta',                   
  author_email = 'imehta34@gatech.edu',      
  url = 'https://github.com/IshMehta/DataStructureViz',   
  download_url = '',    
  keywords = ['data structure', 'graph','list','array','tree','BST','AVL','binary','draw','visualise'],
  install_requires=[    
      'tk',
      'graphviz',
      'pillow'        
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers, students',
    'Topic :: Software Developement :: Helper Tools',
    'License :: OSI Approved :: MIT Licence',
    'Operating System :: OS Independent'
    'Programming Language :: Python :: 3',
  ],
  long_description=long_description,
  long_description_content_type="text/markdown",
  package_dir={'':'DSViz'},
  include_package_data = True,
)
