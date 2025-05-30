=========================
DeepGRP - Reproducibility
=========================

Repository for reproducing results for `DeepGRP`__ publication.

.. __: https://github.com/fhausmann/deepgrp

Installing requirements
=======================

You can install all required packages using `poetry`__ with::

    git clone https://github.com/fhausmann/deepgrp_reproducibility
    cd deepgrp_reproducibility
    poetry install

.. __: https://python-poetry.org/

.. note::
   To fully reproduce the results from the deepgrp paper, you need to have
   a version of `RepeatMasker`__ `here`__ with `cross_match`__ and a version of
   `Repbase`__, which cannot be provided due to licensing restrictions.

   .. __: https://github.com/rmhubley/RepeatMasker
   .. __: https://github.com/fhausmann/deepgrp_reproducibility/blob/master/repeatmasker/
   .. __: http://www.phrap.org/phredphrapconsed.html
   .. __: https://www.girinst.org/repbase/

To use the packages installed via poetry, you have to activate the poetry 
environment via::

    poetry shell
    
or run your command using::

    poetry run <your command>

Getting the data
================

You can download all the required training/testing data and programs needed with
make::

    poetry run make

Warning, this can take a while, depending on your connection.

Reproducing
===========

All results in the paper are generated with hyperparameters in
`best_model.toml`__.

.. __: https://github.com/fhausmann/deepgrp_reproducibility/blob/master/best_model.toml

These hyperparameters were found using the following search space:

+-------------------+-------------------+-----------------------------------------------------------------+
| Parameter         | Parameter Name    | Distribution                                                    |
+===================+===================+=================================================================+
| Window size       | vecsize           | q-normal(:math:`\mu` = 200, :math:`\sigma` = 20, :math:`q` = 2) |
+-------------------+-------------------+-----------------------------------------------------------------+
| Recurrent units   | units             | q-normal(:math:`\mu` = 32, :math:`\sigma` = 5, :math:`q` = 2)   |
+-------------------+-------------------+-----------------------------------------------------------------+
| Dropout           | dropout           | Uniform(:math:`low` = 0, :math:`high` = 0.4)                    |
+-------------------+-------------------+-----------------------------------------------------------------+
| RMSprop momentum  | momentum          | Uniform(:math:`low` = 0, :math:`high` = 1.0)                    |
+-------------------+-------------------+-----------------------------------------------------------------+
| RMSprop decay     | rho               | Uniform(:math:`low` = 0, :math:`high` = 1.0)                    |
+-------------------+-------------------+-----------------------------------------------------------------+
| Learning rate     | learning_rate     | Lognormal(:math:`\mu` = -7, :math:`\sigma` = 0.5)               |
+-------------------+-------------------+-----------------------------------------------------------------+
| Repeat probability|repeat_probability | Uniform(:math:`low` = 0, :math:`high` = 0.49)                   |
| per batch         |                   |                                                                 |
+-------------------+-------------------+-----------------------------------------------------------------+


The performance and benchmarking results can be downloaded as JSON files from `results`__.
All trained models can be found at `models`__.

.. __: https://github.com/fhausmann/deepgrp_reproducibility/blob/master/results
.. __: https://github.com/fhausmann/deepgrp_reproducibility/blob/master/models

Training
--------
Training of DeepGRP can be done with the Jupyter notebook
`Training_deepgrp.ipynb`__
and `dna-nn`__ with `Training_dnabrnn.ipynb`__.

.. __: https://github.com/fhausmann/deepgrp_reproducibility/blob/master/Training_deepgrp.ipynb
.. __: https://github.com/lh3/dna-nn
.. __: https://github.com/fhausmann/deepgrp_reproducibility/blob/master/Training_dnabrnn.ipynb

Benchmark
---------
Benchmark can be done with `Benchmark.ipynb`__.

.. __: https://github.com/fhausmann/deepgrp_reproducibility/blob/master/Benchmark.ipynb

To evaluate the results from the benchmark experiments, use `Evaluation.ipynb`__.

.. __: https://github.com/fhausmann/deepgrp_reproducibility/blob/master/Evaluation.ipynb

Figures
-------
All figures of the paper can be generated with `Figures.ipynb`__.
They will be saved in a `figures` subfolder.

.. __: https://github.com/fhausmann/deepgrp_reproducibility/blob/master/Figures.ipynb
