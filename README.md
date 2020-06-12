# TADE: Stochastic Conformance Checking using Temporal Activity Density Estimation
------------------------------------------

Prototype implementation of TADE as specified in tba. This tool allows conformance checking with a strong emphasis on the temporal perspective. The ``TADE`` module provides two functions. ``train()`` learns activity-related density estimations and ``fitness()`` computes trace-wise conformance scores depending on the collected kernel density estimations. 

If you'd like to learn more about how it works, see References below.

Brought to you by Florian Richter (richter@dbs.ifi.lmu.de).


Usage
-----

To compute the conformance scores, you need a log. We are using logs from the BPI Challenge 2015 as an example. You can download them under: https://data.4tu.nl/repository/collection:event_logs_real

Example
^^^^^^^

    .. code-block:: python

    #!/usr/bin/env python

    from pm4py.objects.log.importer.xes import importer as xes_importer
    log_train = xes_importer.apply("BPIC15_1.xes")
    log_test = xes_importer.apply("BPIC15_2.xes")

    from TADE import TADE
    tade = TADE()
    tade.train(log_train)

    fitness_scores = [tade.fitness(trace) for trace in log_test]
    print(fitness_scores)


References
----------

The algorithm used by ``TADE`` is taken directly from the original paper by Richter, Sontheim, Zellner and Seidl. If you would like to discuss the paper, or corresponding research questions on temporal process mining (we have implemented a few other algorithms as well) please email the authors.
