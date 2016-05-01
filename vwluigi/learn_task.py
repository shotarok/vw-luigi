#!/usr/bin/env python
# coding:utf-8

import os
import os.path
import subprocess

import luigi


class LearnTask(luigi.Task):
    work_dir = luigi.Parameter(default="/tmp/work")
    model_name = luigi.Parameter(default="model.vw")
    train_name = luigi.Parameter(default="train.vw")
    loss_func = luigi.Parameter(default="logistic")

    def requires(self):
        return []

    def output(self):
        model_path = os.path.join(self.work_dir, self.model_name)
        return luigi.LocalTarget(model_path)

    def run(self):
        if not os.path.exists(self.work_dir):
            os.mkdir(self.work_dir)

        model_path = os.path.join(self.work_dir, self.model_name)
        train_path = os.path.join(self.work_dir, self.train_name)
        cmd = "vw {} -f {} --loss_function {}".format(
            train_path,
            model_path,
            self.loss_func,
        )
        subprocess.run(cmd, shell=True, check=True)

if __name__ == "__main__":
    luigi.run()
