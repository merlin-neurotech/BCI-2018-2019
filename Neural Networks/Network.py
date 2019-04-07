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

#Were going to use k-fold cross validation bc we don't have enough data for a validation set
k = 4
num_val_samples = len(traindata)//k #double slash rounds to nearest whole number
num_epochs = 4

for i in range(k):
    print("Processing fold #", i)
    #select current validation set
    xval = traindata[i*num_val_samples: (i+1)*num_val_samples]
    yval = trainlabels[i*num_val_samples: (i+1)*num_val_samples]
    #cut out current validation set
    xdata = np.concatenate([traindata[:i*num_val_samples],traindata[(i+1)*num_val_samples:]], axis=0)
    ydata = np.concatenate([trainlabels[:i*num_val_samples],trainlabels[(i+1)*num_val_samples:]], axis=0)
    kmodel = buildModel(traindata)
    history = kmodel.fit(x=xdata, y=ydata, epochs=num_epochs, batch_size=1, verbose=2, validation_data=(xval, yval))
    print(history.history.keys())
    acc_hist = history.history["accuracy"]
    all_acc_hist.append(acc_hist)
    avg_acc = [np.mean([x[i] for x in all_acc_hist]) for i in range(num_epochs)]
    #val_mse, val_mae = kmodel.evaluate(xval, yval, verbose=0)
    #all_scores.append(val_mae)