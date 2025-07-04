from tensorflow import keras
from tensorflow.keras import layers

def model():
    model = keras.Sequential()
    model.add(layers.Input(shape=(128, 128, 3)))

    model.add(layers.Conv2D(256, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))

    model.add(layers.Conv2D(160, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))

    model.add(layers.Conv2D(96, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))

    model.add(layers.Flatten())
    model.add(layers.Dense(448, activation='relu'))
    model.add(layers.Dropout(0.4))
    model.add(layers.Dense(4, activation='softmax'))  

    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.0002449483373216793),
        loss='categorical_crossentropy',
        metrics=['accuracy'] )

    return model

    import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras_tuner import HyperModel, RandomSearch
import matplotlib.pyplot as plt


image_size = (128, 128)
batch_size = 32

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

val_datagen = ImageDataGenerator(
    rescale=1./255
)

train_generator = train_datagen.flow_from_directory(
    '/kaggle/input/train/train',
    target_size=image_size,
    batch_size=batch_size,
    class_mode='categorical', 
    shuffle=True
)

val_generator = val_datagen.flow_from_directory(
    '/kaggle/input/valval/val',
    target_size=image_size,
    batch_size=batch_size,
    class_mode='categorical',  
    shuffle=True
)

model = build_model_from_best_hparams()  
history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=120
)
plt.plot(history.history['accuracy'], label='Precisió Entrenament')
plt.plot(history.history['val_accuracy'], label='Precisió Validació')
plt.xlabel('Época')
plt.ylabel('Precisió')
plt.legend()
plt.title('Precisió Entrenament vs Validació')
plt.grid()
plt.show()

model.save("modelo_cnn_clasificacion_kaggle_param_120.h5")