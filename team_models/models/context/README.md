# Context Model

Los modelos estan entrenados con un modelo de redes convolucionales, el cual predice de forma binaria a que clase pertenece la imagen(26 tipos), en estilo variable dummy.

La equivalencia es:

```json
{'Affection': 0, 'Anger': 1, 'Annoyance': 2, 'Anticipation': 3, 'Aversion': 4, 'Confidence': 5, 'Disapproval': 6, 'Disconnection': 7, 'Disquietment': 8, 'Doubt/Confusion': 9, 'Embarrassment': 10, 'Engagement': 11, 'Esteem': 12, 'Excitement': 13, 'Fatigue': 14, 'Fear': 15, 'Happiness': 16, 'Pain': 17, 'Peace': 18, 'Pleasure': 19, 'Sadness': 20, 'Sensitivity': 21, 'Suffering': 22, 'Surprise': 23, 'Sympathy': 24, 'Yearning': 25}
```

La entrada del modelo sería una imagen de 128x128 en color (RGB). Además se debe reescalar el color de la imagen a 0-1(anteriormente en 0-255). 

Ejemplo predicción:

### Primero: Definir una metrica custom

```python
from keras import backend

# calculate fbeta score for multi-class/label classification
def fbeta(y_true, y_pred, beta=2):
	# clip predictions
	y_pred = backend.clip(y_pred, 0, 1)
	# calculate elements
	tp = backend.sum(backend.round(backend.clip(y_true * y_pred, 0, 1)), axis=1)
	fp = backend.sum(backend.round(backend.clip(y_pred - y_true, 0, 1)), axis=1)
	fn = backend.sum(backend.round(backend.clip(y_true - y_pred, 0, 1)), axis=1)
	# calculate precision
	p = tp / (tp + fp + backend.epsilon())
	# calculate recall
	r = tp / (tp + fn + backend.epsilon())
	# calculate fbeta, averaged across each class
	bb = beta ** 2
	fbeta_score = backend.mean((1 + bb) * (p * r) / (bb * p + r + backend.epsilon()))
	return fbeta_score
```

### Segundo: Cargar el modelo y la imagen

```python
#Load Model
new_model = tf.keras.models.load_model('score_3249.h5', custom_objects={'fbeta': fbeta})

#Load image
photo = load_img("frame_01.jpg", target_size=(128,128))
# convert to numpy array
photo = img_to_array(photo, dtype='uint8')

X = np.reshape(photo, (1,128,128,3))
```

### Tercero: Hacer las predicciones

```python
tags = new_model.predict(X)
tags.argmax()
```



Una vez obtener la predicción con mayor porcentaje, hacemos el match con la correspondiente etiqueta descrita en el primer bloque. 