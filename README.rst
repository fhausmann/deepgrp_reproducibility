=========================
DeepGRP - Reproducibility
=========================

Repository for reproducing results for `DeepGRP`__ publication
(currently under review).

.. __: https://github.com/fhausmann/deepgrp

Installing requirements
=======================

You can install all required packages using `poetry`__ with::

    git clone https://github.com/fhausmann/deepgrp_reproducibility
    cd deepgrp_reproducibility
    poetry install

.. __: https://python-poetry.org/

Getting the data
================

You can download all required training/testing data and required programs with
make::

    poetry run make

Warning, this can take a while, depending on your connection.

Reproducing
===========

All results in the paper are generated with hyperparameter in
`best_model.toml`__ and can be downloaded as json files from `results`__.
All trained models can be found at `models`__.

.. __: https://github.com/fhausmann/deepgrp_reproducibility/blob/master/best_model.toml
.. __: https://github.com/fhausmann/deepgrp_reproducibility/blob/master/results
.. __: https://github.com/fhausmann/deepgrp_reproducibility/blob/master/models

Training
--------
Training of DeepGRP can be done with the jupyter notebook
`Training_deepgrp.ipynb`__
and `dna-nn`__ with `Training_dnabrnn.ipynb`__.

.. __: https://github.com/fhausmann/deepgrp_reproducibility/blob/master/Training_deepgrp.ipynb
.. __: https://github.com/lh3/dna-nn
.. __: https://github.com/fhausmann/deepgrp_reproducibility/blob/master/Training_dnabrnn.ipynb

Benchmark
---------
Benchmark can be done with `Benchmark.ipynb`__.
To run the benchmarks for the complete genome hg19 please set
``ALL_HG19`` to `true`.

.. __: https://github.com/fhausmann/deepgrp_reproducibility/blob/master/Benchmark.ipynb

Figures
-------
All figures of the paper can be generated with `Figures.ipynb`__.
They will be saved in a `figures` subfolder.

.. __: https://github.com/fhausmann/deepgrp_reproducibility/blob/master/Figures.ipynb
