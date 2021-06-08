# Context Model

Los modelos estan entrenados con un modelo preentrenado de fastai, el cual predice a que clase pertenece la imagen(7 tipos). Que son las siguientes:

```python
learn.data.classes

['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
```

La entrada del modelo sería una imagen de 224x224 en color (RGB). Además se debe normalizar la imagen con imagenet_stats. 

Ejemplo predicción:

### Primero: Cargar el learner

```python
from fastai.vision import *

learn = load_learner("path") #El path a la carpeta donde esta el export.pkl
```

### Segundo: Cargar la imagen y predecir

```python
img1 = open_image("frame_1.jpg")

learn_export.predict(img1)

pred_class, idx_class, preds = learn_export.predict(img1)
#pred_class: Clase predicha
#idx_class: Posición de la clase predicha en el array de clases
#preds: Porcentaje de pertenencia a cada clase
```



Podemos quedarnos solamente con la variable pred_class que tendrá el nombre de la clase predicha para la foto o el array preds que contiene para cada clase que porcentaje de pertenencia tiene.