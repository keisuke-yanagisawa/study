import luigi
import numpy as np

from sklearn import datasets, svm, cross_validation


#Loading Data
data = datasets.load_diabetes()

#[[1,2,3],4,[[5],[6]]] -> [1,2,3,4,5,6]
def flatten_array(array):
    ret = []
    for a in array:
        if hasattr(a, "__iter__"):
            ret+= flatten_array(a)
        else:
            ret.append(a)
    return ret;

class task_param_eval(luigi.Task):
    data = luigi.Parameter()
    C = luigi.FloatParameter()
    gamma = luigi.FloatParameter()

    def requires(self):
        return []
    def output(self):
        return luigi.LocalTarget("temp/%s.txt" % hash( frozenset([self.C, self.gamma]) ))
    def run(self):
        model = svm.SVR(C=self.C, gamma=self.gamma)

        # cross_val_score function returns the "score", not "error". 
        # So, the result is inverse of error value.
        results = -cross_validation.cross_val_score(model, data.data, data.target, scoring="mean_absolute_error")
        with self.output().open("w") as out_file:
            out_file.write( str(np.mean(results)) ); 
        

class task_param_tuning(luigi.Task):

    cost_list = luigi.Parameter(default="1,2,5,10")
    gamma_list = luigi.Parameter(default="1,2,5,10")
    
    data = datasets.load_diabetes()

    def requires(self):
        return flatten_array(
            map(lambda C:
                    map(lambda gamma:
                            task_param_eval(data=frozenset(self.data), # values should be hashable 
                                       C=float(C), gamma=float(gamma)),
                        self.cost_list.split(",")),
                self.gamma_list.split(",")))
    def output(self):
        return luigi.LocalTarget("results.csv")
    def run(self):

        results = {}

        for task in self.requires():
            with task.output().open() as taskfile:
                results[(task.C, task.gamma)] = float(taskfile.read())
        
        best_key = min(results,  key=results.get)
        with self.output().open("w") as out_file:
            out_file.write("%s,%s,%.4f\n" %(best_key[0], best_key[1], results[best_key]))

if __name__ == "__main__":
    luigi.run()
