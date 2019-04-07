from keras import models
from keras import losses

def buildModel(traindata):
    """Builds Neural Network"""
    #since there is not a lot of data, best to have few hidden layers to prevent overfitting
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(traindata.shape[1],)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop', loss=losses.categorical_crossentropy, metrics=["acc"])

    return model


#import and format data
model = buildModel(traindata)
history = model.fit(trainx, trainy, epochs=10, batch_size=32, validation_data=(xval, yval))
results =  model.evaluate(x_test, y_test)
print(results)