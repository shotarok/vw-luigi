#!/usr/bin/env python
# coding:utf-8

import os
import os.path
import subprocess

import luigi

from vwluigi.learn_task import LearnTask


class PredictTask(luigi.Task):
    work_dir = luigi.Parameter(default="/tmp/work")
    model_name = luigi.Parameter(default="model.vw")
    train_name = luigi.Parameter(default="train.vw")
    loss_func = luigi.Parameter(default="logistic")
    test_name = luigi.Parameter(default="test.vw")
    predict_name = luigi.Parameter(default="predict.vw")

    def requires(self):
        return [LearnTask(
            work_dir=self.work_dir,
            model_name=self.model_name,
            train_name=self.train_name,
            loss_func=self.loss_func
        )]

    def output(self):
        predict_path = os.path.join(self.work_dir, self.predict_name)
        return luigi.LocalTarget(predict_path)

    def run(self):
        if not os.path.exists(self.work_dir):
            os.mkdir(self.work_dir)

        model_path = os.path.join(self.work_dir, self.model_name)
        test_path = os.path.join(self.work_dir, self.test_name)
        predict_path = os.path.join(self.work_dir, self.predict_name)
        cmd = "vw {} -i {}  -t -p {} --loss_function {} --link logistic".format(
            test_path,
            model_path,
            predict_path,
            self.loss_func,
        )
        subprocess.run(cmd, shell=True, check=True)


if __name__ == "__main__":
    luigi.run()
