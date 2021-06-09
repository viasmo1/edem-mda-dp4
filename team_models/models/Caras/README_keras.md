# Face Expression Recognition - modelo 1

El modelo esta hecho con fastai a partir de una resnet50 el cual predice 7 emociones. 
[0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral] Se ha entrenado con el 
dataset FER2013.

La entrada sería una imagen de 48x48 en escala de grises. Además se debe reescalar el color de la 
imagen a 0-1(anteriormente en 0-255).

1. dataset: 

\datasets\caras_keras\fer2013.csv

2. preprocesamiento de datos: 

training = data.loc[data["Usage"] == "Training"]
public_test = data.loc[data["Usage"] == "PublicTest"]
private_test = data.loc[data["Usage"] == "PrivateTest"]

train_labels = training["emotion"]
train_labels = to_categorical(train_labels)

val_labels = private_test["emotion"]
val_labels = to_categorical(val_labels)

test_labels = public_test["emotion"]
test_labels = to_categorical(test_labels)

train_images = training["pixels"].str.split(" ").tolist()
train_images = np.uint8(train_images)
train_images = train_images.reshape((train_images.shape[0], 48, 48, 1))
train_images = train_images.astype('float32')/255

val_images = private_test["pixels"].str.split(" ").tolist()
val_images = np.uint8(val_images)
val_images = val_images.reshape((val_images.shape[0], 48, 48, 1))
val_images = val_images.astype('float32')/255

test_images = public_test["pixels"].str.split(" ").tolist()
test_images = np.uint8(test_images)
test_images = test_images.reshape((test_images.shape[0], 48, 48, 1))
test_images = test_images.astype('float32')/255

4. Data aumentation

datagen = ImageDataGenerator(
    rotation_range=15,
    width_shift_range=0.15,
    height_shift_range=0.15,
    shear_range=0.15,
    zoom_range=0.15,
    horizontal_flip=True,)

datagen.fit(train_images)

5. Recorte de la cara:

notebook = recorte__foto.ipynb

hacer resize a 48x48 y escalar dividiendo por 255

6. Predicción 
