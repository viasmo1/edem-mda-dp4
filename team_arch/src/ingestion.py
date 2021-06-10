import os
import requests
from zipfile import ZipFile
from io import BytesIO

# import numpy as np
# import pandas as pd
# import cv2

url = "https://github.com/lggx/Face_expression_recognition/raw/main/fer2013.zip"
response = requests.get(url)

z = ZipFile(BytesIO(response.content))
z.extractall("./images/initial_dataset")

os.chdir("./images/initial_dataset")

"""
data = pd.read_csv("fer2013.csv")

data["pixels_graph"] = data["pixels"].apply(lambda x: x.split(" "))
data["pixels_graph"] = data["pixels_graph"].apply(lambda x: np.reshape(x, (48, 48)))
data["pixels_graph"] = data["pixels_graph"].apply(lambda x: x.astype(int))

data.to_csv("fer2013_images.csv", index=False)


for index, row in data.iterrows():
    pic_name = f"{index}.jpg"
    cv2.imwrite(pic_name, row["pixels_graph"])
"""
