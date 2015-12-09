import luigi

class simple_task(luigi.Task):
    number = luigi.IntParameter()
    def output(self):
        return luigi.LocalTarget("temp/%d.csv" % self.number)
    def run(self):
        with self.output().open("w") as out_file:
            out_file.write("%d" % self.number)

class main_task(luigi.Task):
    number = luigi.IntParameter()
    def requires(self):
        return map(lambda x: simple_task(number=x), range(self.number))

    def output(self):
        return luigi.LocalTarget("temp/dummy.csv")
    def run(self):
        with self.output().open("w") as out_file:
            out_file.write("dummy")

if __name__ == "__main__":
    luigi.run()
