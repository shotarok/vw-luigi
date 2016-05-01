#!/usr/bin/env
# coding:utf-8

import os
import os.path

import luigi

from vwluigi.predict_task import PredictTask
from vwluigi.util import vweval


class EvalTask(luigi.Task):
    work_dir = luigi.Parameter(default="/tmp/work")
    model_name = luigi.Parameter(default="model.vw")
    train_name = luigi.Parameter(default="train.vw")
    loss_func = luigi.Parameter(default="logistic")
    test_name = luigi.Parameter(default="test.vw")
    predict_name = luigi.Parameter(default="predict.vw")
    result_name = luigi.Parameter(default="result.txt")

    def requires(self):
        return [PredictTask(
            work_dir=self.work_dir,
            model_name=self.model_name,
            train_name=self.train_name,
            test_name=self.test_name,
            predict_name=self.predict_name,
            loss_func=self.loss_func,
        )]

    def output(self):
        result_path = os.path.join(self.work_dir, self.result_name)
        return luigi.LocalTarget(result_path)

    def run(self):
        predict_path = os.path.join(self.work_dir, self.predict_name)
        test_path = os.path.join(self.work_dir, self.test_name)
        result_path = os.path.join(self.work_dir, self.result_name)
        vweval(test_path, predict_path, result_path)
