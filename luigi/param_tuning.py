import re

import luigi
import numpy as np
import pandas as pd

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

def convert2num(c):
    # https://github.com/pydata/pandas/issues/9589                                                                     
    try:
        return c.astype(np.number)
    except:
        return c

# common task class for parameter tuning.
class param_tuning(luigi.Task):
    tasks        = luigi.Parameter()
    text_format  = luigi.Parameter()
    reduce_pivot = luigi.Parameter()
    reduce_rule  = luigi.Parameter(default="min")
    out_file     = luigi.Parameter()

    def requires(self):
        return self.tasks;
    def output(self):
        return luigi.LocalTarget(self.out_file)
    def run(self):
        results = []
        for task in self.requires():
            with task.output().open() as taskfile:
                string = taskfile.read()
                groupdict = re.search(self.text_format, string).groupdict()
                results.append(groupdict)

        # making pandas dataframe
        df = pd.DataFrame.from_dict(results);
        df[self.reduce_pivot] = convert2num(df[self.reduce_pivot])
        values = df[self.reduce_pivot]

        # Arrangement of column order
        column_order = filter(lambda key: key != self.reduce_pivot, df.columns) + [self.reduce_pivot]
        df = df[column_order]

        if self.reduce_rule == "min":
            best_val = min(values)
        elif self.reduce_rule == "max":
            best_val = max(values)
        else:
            print("reduce_rule must be min or max. your input is %s" % self.reduce_rule)
            exit(1);

        df[df[self.reduce_pivot] == best_val].to_csv(self.output().fn, index=False);


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
            out_string = "%f,%f,%f" % (self.C, self.gamma, np.mean(results))
            out_file.write(out_string); 

class main_task(luigi.Task):
    cost_list = luigi.Parameter(default="1,2,5,10,20,50,100,200,500,1000,2000,5000,10000")
    gamma_list = luigi.Parameter(default="1,2,5,10,20,50,100,200,500,1000,2000,5000,10000")
    
    data = datasets.load_diabetes()

    def requires(self):
        costs  = self.cost_list.split(",")
        gammas = self.gamma_list.split(",")

        tasks = flatten_array(
            map(lambda C: map(lambda gamma:
                    task_param_eval(data=frozenset(self.data), # values should be hashable 
                                    C=float(C), gamma=float(gamma)),
                costs), gammas))

        s = "[-+]?\d*\.\d+|\d+" ## float or int expression
        return param_tuning(tasks        = tasks,
                            text_format  = "(?P<cost>"+s+"),(?P<gamma>"+s+"),(?P<error>"+s+")",
                            reduce_pivot = "error",
                            reduce_rule  = "min",
                            out_file     = "result.csv")

if __name__ == "__main__":
    luigi.run()
