# FunWithTSER
Let's have some fun with the Time Series Extrinsic Regression (TSER) Dataset.

**⚠️ Warnings ⚠️**
* This is a weekend research project, not a deep scientific analysis.
* No search for hyperparameters has been made, the training parameters of the models are chosen empirically.
* This is an experimental repository, do not use the code without checking it first.

**Quick conclusions and Remarks**
* Constant model (mean of training set) baseline is better than anything on one dataset and very close to the SOTA on other dataset.
  * We are clearly not doing much better than a naive model...
* The number of filters per layer impact is relatively small (e.g. CMV1-XS versus CMV1-L in [results](#results) section).
* The results stability is quite bad, most of model have a ±50% potential shift (unmeasured).
  During my first tests (undocumented and before any commit), I had very very good results, but I haven't reproduced them since,
  I don't really know what I was doing back then, but CMV0 was very close to Inception.
* As said in the [dataset](#dataset) section, we only work on a subset of the TSER dataset.

### Results
* Evaluation : 5 run average RMSE score.
  * If score is *italic*, there is less than 5 runs.
  * If score is **bold**, results are better than state of the art.
* FCN, ResNet and Inception results came from the dataset web page, more results in the [full benchmark](#full-benchmark) section.
* Baselines : as I'm not an expert on the dataset and I may have made errors, I create this baselines scores using my metric implementation to have some ideas of expected values.
  * Constant : a constant model always predicting train set mean value.
  * 5% : a near perfect model predicting test set values ±5%.
  * SkResNet : [`sktime.regression.deep_learning.resnet.ResNetRegressor`](https://www.sktime.net/en/latest/api_reference/auto_generated/sktime.regression.deep_learning.ResNetRegressor.html) params±500k.
    Even if only 20 epochs are performed, training is very long compared to CMNet models, I don't know why exactly and didn't checked sktime implementation.
* CMNet : custom model I tryed.
  * CMV1 : FCN like convolutional neural network architecture with conv block and pooling, see [CMV1.ipynb](CMV1.ipynb). Score calculated on 3 runs.
    * CMV1-XS : ±3k parameters
    * CMV1-S  : ±12k parameters
    * CMV1    : ±50k parameters
    * CMV1-L  : ±445k parameters, tend to have as much parameters as SkResNet baseline.
  * CMV2 : Like CMV1 with larger convolution kernels, see [CMV2.ipynb](CMV2.ipynb).
    * CMV2-5 : ±83k parameters
    * CMV2-7 : ±116k parameters
    * CMV2-9 : ±150k parameters

| **Dataset Name** | **FCN**   | **ResNet** | **Inception** | **Constant** | **5%**   | **SkResNet** |
| ---------------- | ---------:| ----------:| -------------:| ------------:| --------:| ------------:|
| BIDMC32HR        | 13,1306   | 10,7414    |  9,4246       | 14,1101      | *2,5800* | 10,2471      |
| BIDMC32RR        |  3,5777   |  3,9212    |  3,0184       |  3,4967      | *0,5172* |  3.9523      |
| BIDMC32SpO2      |  5,9683   |  5,9878    |  5,5761       |**4,8029**    | *2,8098* |  5.5308      |

| **Dataset Name** | **CMV1**  | **CMV1-XS** | **CMV1-S** | **CMV1-L** | **CMV2-5** | **CMV2-7** | **CMV2-9** |
| ---------------- | ---------:| -----------:| ----------:| ----------:| ----------:| ----------:| ----------:|
| BIDMC32HR        | *12.7861* | *11.2989*   | *14.4698*  | *12.2512*  | **8.5722** | **8.5640** | **8.8000** |
| BIDMC32RR        |  *5.1015* |  *5.5134*   |  *5.1234*  |  *5.1770*  |   6.1946   |   5.8331   |   5.2203   |
| BIDMC32SpO2      |  *5.5143* |  *5.7413*   |  *5.0580*  |***4.6425***| **5.4383** | **5.4139** |   6.1529   |

### Full benchmark
* Source : http://tseregression.org/

| **Dataset Name** | **FPCR**  | **FPCR-Bspline** | **SVR**   | **SVR Optimised** | **Random Forest** | **XGBoost** | **1-NN-ED** | **5-NN-ED** | **1-NN-DTWD** | **5-NN-DTWD** | **Rocket** | **FCN**   | **ResNet** | **Inception** |
| ---------------- | --------- | ---------------- | --------- | ----------------- | ----------------- | ----------- | ----------- | ----------- | ------------- | ------------- | ---------- | --------- | ---------- | ------------- |
| BIDMC32HR        | 13,980558 | 13,980597        | 13,579905 | 13,39297          | 15,016468         | 13,963799   | 14,836506   | 14,756088   | 15,29101      | 15,127008     | 13,9443828 | 13,130665 | 10,74142   | 9,424679      |
| BIDMC32RR        | 3,364777  | 3,364704         | 4,160427  | 3,17366           | 4,350314          | 4,367828    | 4,387345    | 4,134685    | 3,529111      | 3,432247      | 4,0929006  | 3,577775  | 3,921214   | 3,018405      |
| BIDMC32SpO2      | 4,953519  | 4,953517         | 4,818862  | 4,796855          | 4,570262          | 4,450805    | 5,530202    | 5,407875    | 5,215027      | 5,123964      | 5,221737   | 5,968337  | 5,987832   | 5,57612       |

### Dataset
For now, I only selected the BIDMC subpart of TSER dataset.
I originally selected this subpart in particular as it is the only one where the paper specified "manually annotated" (see references).

| ID | Type              | Dataset   | Train | Test | Length | Missing Values | Dimension | Description                                             |
| -- | ----------------- | --------- | ----- | ---- | ------ | -------------- | --------- | ------------------------------------------------------- |
| 14 | Health Monitoring | BIDMCRR   | 5471  | 2399 | 4000   | No             | 2         | Predict breathing rate using PPG and ECG                |
| 15 | Health Monitoring | BIDMCHR   | 5550  | 2399 | 4000   | No             | 2         | Predict heart rate using PPG and ECG                    |
| 16 | Health Monitoring | BIDMCSpO2 | 5550  | 2399 | 4000   | No             | 2         | Predict blood oxygen saturation level using PPG and ECG |

### References
* Paper
  * [Monash University, UEA, UCR Time Series Extrinsic Regression Archive](https://arxiv.org/abs/2006.10996)
* Website
  * [TSERegression.org](http://tseregression.org/)
