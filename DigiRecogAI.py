from email.mime import image
from genericpath import isfile
import os;
import cv2;
import numpy as np;
import matplotlib.pyplot as plt;
import tensorflow as tf;

mnist = tf.keras.datasets.mnist;
(x_train,y_train) , (x_test,y_test) = mnist.load_data();

x_train = tf.keras.utils.normalize (x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test,axis=1)

# model = tf.keras.models.Sequential()
# model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
# model.add(tf.keras.layers.Dense(128,activation= 'relu'))
# model.add(tf.keras.layers.Dense(128,activation= 'relu'))
# model.add(tf.keras.layers.Dense(10,activation= 'softmax'))

# model.compile(optimizer ='adam',loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# model.fit(x_train,y_train, epochs =5)
# model.save('handwritten.keras')

model = tf.keras.models.load_model('handwritten.keras')
# loss, accuracy = model.evaluate(x_test,y_test)
# print(loss)
# print(accuracy)

image_number =1
while os.path.isfile(f"Digits/digit{image_number}.png"):
  try:
      img =cv2.imread(f"Digits/digit{image_number}.png")[:,:,0]
      img = np.invert(np.array([img]))
      prediction= model.predict(img)
      print(f"This digit is probably a: {np.argmax(prediction)}")
      # Correct way to show an image with a colormap
      plt.imshow(img[0], cmap=plt.cm.binary)
      plt.show()
  except:
     print("error")
  finally:
     image_number +=1    