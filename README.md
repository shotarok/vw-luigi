# vw-luigi
> luigi workflows to evaluate models trained by vowpal wabbit.

![gif](https://gyazo.com/a86de7b93a18d990249176a8f6ba54ed.gif)

## Installation of Prerequisite softwares

If you'd like to use vw-luigi, you need to install *vowpal wabbit* and some python modules.

### vowpal wabbit
See https://github.com/JohnLangford/vowpal_wabbit.  
If you use OSX, you can install vowpal-wabbit through homebrew.
```shell
brew install vowpal-wabbit
```

### python modules
Workflows in vw-luigi depend on *luigi*, *numpy* and *scikit-learn*. You can install required modules through pip.
```shell
pip install -r requirements.txt
```

## Usage Example

In case you use `/tmp/work/space/train.vw` as training data, `/tmp/work/space/test.vw` as test data and *squared loss* as loss function, you can get the evaluation result, which includes AUROC, AUPR and LossLoss calculated by *scikit-learn*, following to below commands.

```shell
$ cd vw-luigi
$ ls /tmp/work/space
> train.vw test.vw
$ python -m luigi --module vwluigi EvalTask --loss-func squared --work-dir /tmp/work/space --local-scheduler
> ...
$ ls /tmp/work/space
> model.vw predict.vw result.txt train.vw
$ cat /tmp/work/space/result.txt
> AUROC:0.88060 AUPR:0.72192 LOGLOSS:0.36215
```

If you are interested in vw-luigi, please see this blog post ["'Kaggle Display Advertising Challenge' working with vw-luigi"](http://blog.shotarok.com/post/2016-05-03-vwluigi_with_critio_dataset/). I wrote another usage example using ['Kaggle Display Advertising Challenge Dataset'](http://criteolabs.wpengine.com/downloads/2014-kaggle-display-advertising-challenge-dataset/) provided by Critio.
## Release History

* 0.1.0
   * The first proper release

## Meta
Distributed under the MIT license.  See `LICENSE` for more information.  
Author: Shotaro Kohama - tw: [@shotarok28](https://twitter.com/shotarok28)
