# Face Expression Recognition - modelo 1

El modelo esta hecho con fastai a partir de una resnet50 el cual predice 7 emociones. 
[0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral] Se ha entrenado con el 
dataset FER2013.

La entrada sería una imagen de 48x48 en escala de grises. Además se debe reescalar el color de la 
imagen a 0-1(anteriormente en 0-255).


