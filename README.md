# FunWithTSER
Let's have some fun with the Time Series Extrinsic Regression (TSER) Dataset

### Results
* Evaluation : 5 run average RMSE score.
  * If score is in *italic*, there is less than 5 runs.
* FCN, ResNet and Inception results came from the dataset web page, more results in the [full benchmark](#full-benchmark) section.
* Baselines : as I'm not an expert on the dataset and I may have made errors, I create this baselines scores using my metric implementation.
  * Constant : a constant model always predicting train set mean value.
  * 5% : a near perfect model predicting test set values ±5%.
  * SkResNetRegressor : [`sktime.regression.deep_learning.resnet.ResNetRegressor`](https://www.sktime.net/en/latest/api_reference/auto_generated/sktime.regression.deep_learning.ResNetRegressor.html) params±500k, batch_size=4, n_epochs=20.
* CMNet : custom model I tryed.
  * CMV1
  * CMV1-Tank : Same as CMV1 with as much parameters as possible on my setup (RTX 2080 ti)

| **Dataset Name** | **FCN**   | **ResNet** | **Inception** | **Constant** | **5%**   | **SkResNetRegressor** | **CMV1** |
| ---------------- | --------- | ---------- | ------------- | ------------ | -------- | --------------------- | -------- |
| BIDMC32HR        | 13,1306   | 10,7414    |  9,4246       | 14,1101      | *2.5800* |                       |          |
| BIDMC32RR        |  3,5777   |  3,9212    |  3,0184       |  3,4967      | *0.5172* |                       |          |
| BIDMC32SpO2      |  5,9683   |  5,9878    |  5,5761       |  4,8029      | *2.8098* |                       |          |

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
