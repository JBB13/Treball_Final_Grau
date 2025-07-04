import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras_tuner import HyperModel, RandomSearch

image_size = (128, 128)
batch_size = 32

train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

train_generator = train_datagen.flow_from_directory(
    r'C:\Users\janbi\Desktop\pen\SanDisk\documentos\Universitat\UPC\Q8\TFG\imatges\imatges_algoritme_class\train',
    target_size=image_size,
    batch_size=batch_size,
    class_mode='categorical',
    subset='training',
    shuffle=True
)

val_generator = train_datagen.flow_from_directory(
    r'C:\Users\janbi\Desktop\pen\SanDisk\documentos\Universitat\UPC\Q8\TFG\imatges\imatges_algoritme_class\val',
    target_size=image_size,
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation',
    shuffle=True
)

class CNNHyperModel(HyperModel):
    def build(self, hp):
        model = keras.Sequential()
        model.add(layers.Input(shape=(128, 128, 3)))

        for i in range(hp.Int('num_conv_blocks', 2, 4)):
            model.add(layers.Conv2D(
                filters=hp.Int(f'filters_{i}', 32, 256, step=32),
                kernel_size=(3, 3),
                activation='relu'
            ))
            model.add(layers.MaxPooling2D((2, 2)))

        model.add(layers.Flatten())
        model.add(layers.Dense(
            units=hp.Int('dense_units', 64, 512, step=64),
            activation='relu'
        ))
        model.add(layers.Dropout(hp.Float('dropout_rate', 0.3, 0.7, step=0.1)))
        model.add(layers.Dense(4, activation='softmax'))

        model.compile(
            optimizer=keras.optimizers.Adam(
                hp.Float('learning_rate', 1e-4, 1e-2, sampling='log')
            ),
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )

        return model

hypermodel = CNNHyperModel()
tuner = RandomSearch(
    hypermodel,
    objective='val_accuracy',
    max_trials=20,
    executions_per_trial=1,
    directory='cnn_tuner_dir',
    project_name='cnn_opt'
)


tuner.search(
    train_generator,
    validation_data=val_generator,
    epochs=30
)


print("\Millors Hiperparametres:")
best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]
print(best_hps.values)