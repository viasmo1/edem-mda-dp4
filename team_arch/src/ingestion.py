import os
import requests

print(os.getcwd())
os.chdir("images")
print(os.listdir())

url = "https://i.pinimg.com/originals/83/f9/37/83f937b69f30bb886ab8a03390da6771.jpg"
page = requests.get(url)

f_ext = os.path.splitext(url)[-1]

with open("test.jpg", "wb") as file_to_save:
    file_to_save.write(page.content)

print(os.listdir())
