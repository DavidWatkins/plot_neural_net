#!/usr/bin/env python

from distutils.core import setup

setup(name='plot_neural_net',
      version='1.0',
      description='Plot a neural network',
      package_dir={'': 'src'},
      packages=['plot_neural_net'],
      install_requires=[
          'pdflatex',
      ],
      )
