import tensorflow as tf

modelo = tf.keras.models.load_model("modelo_cnn_clasificacion_kaggle_param_120.h5")


converter = tf.lite.TFLiteConverter.from_keras_model(modelo)
converter.optimizations = [tf.lite.Optimize.DEFAULT]  
converter.target_spec.supported_types = [tf.float16]
converter.experimental_new_converter = True 


tflite_model = converter.convert()
with open("modelo_cnn_clasificacion_kaggle_param_120_quant.tflite", "wb") as f:
    f.write(tflite_model)