Different number of various kind of layers and number of filters and neurons was experimented to improve the accuracy with less loss. 
At first, I got `loss: 3.4952 - accuracy: 0.0532` with the follwing setting:
* 1 convolution layer, 32 (3x3) filters
* 1 pooling layer, size (2x2)
* 1 hidden layer, 128 units with 0.5 dropout

One hidden layer probably not enough to handle this complex dataset. Therefore, 2 hidden layer with 128 units was added to the model, resulting in `loss: 0.5934 - accuracy: 0.8901`. The addition of hidden layer probably helped the model handling the traffic signs better. A 0.5 dropout after all the hidden layer was added to prevent overfitting. Finally, I tried adding one convolution layer and 1 pooling layer to make neural networks less sensitive to variation. This final setting have `loss: 0.1137 - accuracy: 0.9759`, which shows the addition of convolution layer and pooling layer did helps the model to handle the variation in images of the same sign.