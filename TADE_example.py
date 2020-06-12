from pm4py.objects.log.importer.xes import importer as xes_importer
log_train = xes_importer.apply("BPIC15_1.xes")
log_test = xes_importer.apply("BPIC15_2.xes")

from TADE import TADE
tade = TADE()
tade.train(log_train)

fitness_scores = [tade.fitness(trace) for trace in log_test]
print(fitness_scores)