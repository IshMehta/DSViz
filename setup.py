from distutils.core import setup

setup(
  packages = ['DSViz'],   
  name = 'DSViz',       
  version = '0.1',      
  license='MIT',        
  description = 'DSViz is a simple and intuitive Python interface to multiple packages in order to help visualise different data structres while coding them. This package is developed mainly for students or developers who are in the process of learning data structures.',   # Give a short description about your library
  author = 'Ish Mehta <ish.mehta2310@gmail.com>, Krisha Vekaria <kbv5097@psu.edu>',                   
  author_email = 'ish.mehta2310@gmail.com',      
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
    'License :: MIT Licence',
    'Programming Language :: Python :: 3',
  ],
)
