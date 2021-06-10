import os
import requests
from zipfile import ZipFile
from io import BytesIO

url = "https://github.com/lggx/Face_expression_recognition/raw/main/fer2013.zip"
response = requests.get(url)

z = ZipFile(BytesIO(response.content))
z.extractall("./images/initial_dataset")
