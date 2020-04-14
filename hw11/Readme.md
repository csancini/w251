## Homework 11 Answers

#### Successful landings video clips

Bucket: https://s3.us.cloud-object-storage.appdomain.cloud/cs-w251-hw11/landings.tgz

The video clips can also be found here: [Clip 1](export_landing_1.mp4) [Clip 2](export_landing_2.mp4) [Clip 3](export_landing_3.mp4) [Clip 4](export_landing_4.mp4)  [Clip 5](export_landing_5.mp4)  

#### Model Tweaks

The model improvement was achieved through several changes in the model structure and hyperparameters. First, the loss funcion was changed to ```mean absolute error```, since this metric better represents the cumulative reward system of the reinforcement learning task. This was the single thing that caused the highest improvement in the model. Second, the input layer was increased to ```600``` activations and the following layer to ```150``` (further increase in the number of activatons or the number of layers did not improve the model). All layers were also interleaved with ```batch normalization``` and configured with the ```tanh``` non-linearity. Third, the optimizer was changed to ```Adamax``` with a ```higher learning rate``` equal to ```0.01```. The number of epochs wass also changed to ```20```. This combination caused the mean absolute error to decrease faster during the training step. Fourth, ```L2 regularization``` was added to all layers of the model with a factor of ```0.001``` to help the model generalize better.
