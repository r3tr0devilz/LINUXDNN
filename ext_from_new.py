import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing

path2 = "/data2/Users/undergraduate/bharadwaj/csvfiles/G12/data/"

sig_final = pd.read_csv(path2+'sig.csv')
bkg_final = pd.read_csv(path2+'bkg.csv')
data_df = pd.concat([sig_final,bkg_final],ignore_index = True)
print(data_df.shape)
data = data_df.values

inds = np.arange(data.shape[0])
tr   = int(0.6 * data.shape[0]) 
np.random.RandomState(11).shuffle(inds)

train_data = data[inds[:tr]]
rest_data   = data[inds[tr:]]
val_data = rest_data[:int(rest_data.shape[0] /2)]
test_data = rest_data[int(rest_data.shape[0] /2):]


np.savetxt(path2+'train_data.csv',train_data,fmt='%5.5f',header = "phoHoverE,phoTrkSumPtHollowConeDR03,phoPFClusEcalIso,phoPFClusHcalIso,phoEoverphoraw,phoE2ndoverphoraw,phoE2x2overphoraw,phoE1x3overphoraw,phoE2x5overphoraw,phoE5x5overphoraw,phoSigmaIEtaIEtaFull5x5,phoSigmaIPhiIPhiFull5x5,phoSigmaIEtaIPhiFull5x5,Weights,isSignal",delimiter = ',',comments = "")

np.savetxt(path2+'val_data.csv',val_data,fmt = '%5.5f',header = "phoHoverE,phoTrkSumPtHollowConeDR03,phoPFClusEcalIso,phoPFClusHcalIso,phoEoverphoraw,phoE2ndoverphoraw,phoE2x2overphoraw,phoE1x3overphoraw,phoE2x5overphoraw,phoE5x5overphoraw,phoSigmaIEtaIEtaFull5x5,phoSigmaIPhiIPhiFull5x5,phoSigmaIEtaIPhiFull5x5,Weights,isSignal" , delimiter = ',', comments = "")

np.savetxt(path2+'test_data.csv',test_data,fmt = '%5.5f',header = "phoHoverE,phoTrkSumPtHollowConeDR03,phoPFClusEcalIso,phoPFClusHcalIso,phoEoverphoraw,phoE2ndoverphoraw,phoE2x2overphoraw,phoE1x3overphoraw,phoE2x5overphoraw,phoE5x5overphoraw,phoSigmaIEtaIEtaFull5x5,phoSigmaIPhiIPhiFull5x5,phoSigmaIEtaIPhiFull5x5,Weights,isSignal",delimiter = ',',comments = "")

train_data = pd.read_csv(path2+'train_data.csv')
test_data = pd.read_csv(path2+'test_data.csv')
val_data = pd.read_csv(path2+'val_data.csv')

weight = train_data['Weights']
train_weight = weight.to_numpy()


x_train2 = train_data.iloc[:,:-2]
y_train = train_data['isSignal']

x_test2= test_data.iloc[:,:-2]
y_test = test_data['isSignal']

x_val2 = val_data.iloc[:,:-2]
y_val = val_data['isSignal']



standardscaler = preprocessing.StandardScaler()

x_train = standardscaler.fit_transform(x_train2)

x_test = standardscaler.transform(x_test2)

x_val = standardscaler.transform(x_val2)

np.savetxt(path2+'train_scaler_data.csv',x_train,fmt='%5.5f',header='phoHoverE,phoTrkSumPtHollowConeDR03,phoPFClusEcalIso,phoPFClusHcalIso,phoEoverphoraw,phoE2ndoverphoraw,phoE2x2overphoraw,phoE1x3overphoraw,phoE2x5overphoraw,phoE5x5overphoraw,phoSigmaIEtaIEtaFull5x5,phoSigmaIPhiIPhiFull5x5,phoSigmaIEtaIPhiFull5x5',delimiter =',',comments = '')

np.savetxt(path2+'val_scaler_data.csv',x_val,fmt='%5.5f',header='phoHoverE,phoTrkSumPtHollowConeDR03,phoPFClusEcalIso,phoPFClusHcalIso,phoEoverphoraw,phoE2ndoverphoraw,phoE2x2overphoraw,phoE1x3overphoraw,phoE2x5overphoraw,phoE5x5overphoraw,phoSigmaIEtaIEtaFull5x5,phoSigmaIPhiIPhiFull5x5,phoSigmaIEtaIPhiFull5x5',delimiter =',',comments = '')

np.savetxt(path2+'test_scaler_data.csv',x_test,fmt='%5.5f',header='phoHoverE,phoTrkSumPtHollowConeDR03,phoPFClusEcalIso,phoPFClusHcalIso,phoEoverphoraw,phoE2ndoverphoraw,phoE2x2overphoraw,phoE1x3overphoraw,phoE2x5overphoraw,phoE5x5overphoraw,phoSigmaIEtaIEtaFull5x5,phoSigmaIPhiIPhiFull5x5,phoSigmaIEtaIPhiFull5x5',delimiter =',',comments = '')

x_train = pd.read_csv(path2+'train_scaler_data.csv')
x_test = pd.read_csv(path2+'test_scaler_data.csv')
x_val = pd.read_csv(path2+'val_scaler_data.csv')

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--batch', type = int, default = 512,
                   help="--batch 'batch size'")
parser.add_argument('--epoch', type = int, default = 50,
                   help="--epoch 'training epoch'")
parser.add_argument('--neurons', type = int, default = 512,
                   help="--neurons 'N of neurons per layer'")

args, unknown = parser.parse_known_args()

if __name__ == '__main__':

    print("_____Data is being loaded____")


    print(" ")
    print(" ---- END data loading ---- ")

    print(x_train.shape)
    print(x_val.shape)
    print(x_test.shape)
    print(" ")

    batch_size = args.batch
    training_epochs = args.epoch
    neu = args.neurons

    x = layers.Input(shape=[len(x_train.keys())])

    h = layers.Dense(neu, activation = 'relu')(x)
    h = layers.Dropout(0.5)(h)
    h = layers.BatchNormalization()(h)

    h = layers.Dense(neu, activation = 'relu')(h)
    h = layers.Dropout(0.5)(h)
    h = layers.BatchNormalization()(h)

    h = layers.Dense(neu, activation = 'relu')(h)
    h = layers.Dropout(0.5)(h)
    h = layers.BatchNormalization()(h)

    h = layers.Dense(neu, activation = 'relu')(h)
    h = layers.Dropout(0.5)(h)
    h = layers.BatchNormalization()(h)

    h = layers.Dense(neu, activation = 'relu')(h)
    h = layers.Dropout(0.5)(h)
    h = layers.BatchNormalization()(h)

    h = layers.Dense(neu, activation = 'relu')(h)
    h = layers.Dropout(0.5)(h)
    h = layers.BatchNormalization()(h)

    h = layers.Dense(neu, activation = 'relu')(h)
    h = layers.Dropout(0.5)(h)
    h = layers.BatchNormalization()(h)


    h = layers.Dense(neu, activation = 'relu')(h)
    y = layers.Dense(1, activation='sigmoid')(h)

    model = tf.keras.Model(inputs = x, outputs = y)
    model.summary()
    model.compile(optimizer = 'adam',
                 loss = 'binary_crossentropy',
                 metrics=['accuracy']
                 )



    model_weights = 'model_weight_log.h5'
    predictions_file = 'prediction_nn_log.pyc'

    from keras.callbacks import CSVLogger
    csv_logger = CSVLogger('train_log.csv', append = True, separator=',')

#     try:
#         model.load_weights(model_weights)
#         print('Weights loaded from'+ model_weights)
#     except IOError:
#         print ('No pre-trained weights found')
    try:
        history = model.fit(x_train, y_train,
                 batch_size=batch_size,
                 epochs=training_epochs,
                 verbose=1,
                 sample_weight = train_weight,
                 #class_weight = {0: 10101/17868, 1: 1},
                 callbacks=[
                     tf.keras.callbacks.EarlyStopping(verbose=True, patience=10, monitor='val_loss'),
                     tf.keras.callbacks.ModelCheckpoint(model_weights,
                     monitor='val_loss', verbose = True, save_best_only=True),
                     csv_logger
                 ],
                 validation_data=(x_val,y_val)
            )
    except KeyboardInterrupt:
        print ('Training Finished early')

    model.load_weights(model_weights)
    yhat = model.predict(x_test, verbose = 1, batch_size = batch_size)
    np.save(predictions_file,yhat)

    test_loss, test_acc = model.evaluate(x_test,y_test)
    print('test_acc:', test_acc)

