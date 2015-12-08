import luigi
import luigi.mock

class mock_task(luigi.Task):
    def output(self):
        return luigi.mock.MockTarget("hoge.csv")
    def run(self):
        with self.output().open("w") as out_file:
            out_file.write(",".join(["1"]*100000000))

class local_task(luigi.Task):
    def output(self):
        return luigi.LocalTarget("hoge.csv")
    def run(self):
        with self.output().open("w") as out_file:
            out_file.write(",".join(["1"]*100000000))

class main(luigi.Task):
    usemock = luigi.BoolParameter()
    def requires(self):
        if self.usemock:
            return mock_task()
        else:
            return local_task()
    def output(self):
        return luigi.LocalTarget("test.csv");
    def run(self):
        with self.input().open("r") as in_file:
            a = in_file.read()
        with self.output().open("w") as out_file:
            out_file.write("%s" % len(a))


if __name__ == "__main__":
    luigi.run()
