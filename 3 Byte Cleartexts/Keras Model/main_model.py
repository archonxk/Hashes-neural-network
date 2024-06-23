import numpy as np 
import tensorflow as tf 
import os
import json
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import gc
from sklearn.preprocessing import LabelEncoder

print("Libraries imported")

cwd = os.getcwd()
path_of_hashes = os.path.join(cwd , "main.txt")

model = tf.keras.Sequential(
    [
        tf.keras.layers.Input(shape=(1,),),
        tf.keras.layers.Dense(256 , activation="linear"),
        tf.keras.layers.Dense(256 , activation="relu"),
        tf.keras.layers.Dense(256 , activation="linear"),
        tf.keras.layers.Dense(1 , activation="sigmoid")
        
    ]
)
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

print("MODEL DEFINED")

f = open(path_of_hashes , "r")
for line in f:
    hash_arr = json.loads(line)
    for dictionary in hash_arr:
        hashed_value = np.array([int(dictionary["hash"].strip())])
        clear_bits = np.array([int(dictionary["clearbits"].strip())])

        model.fit(x=hashed_value.astype(object) , y=clear_bits.astype(object) , epochs=3, batch_size=256 , verbose=1 )
    
    gc.collect()

model.save(os.path.join(cwd , "main_model.keras"))