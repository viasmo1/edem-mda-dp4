import os
import requests

os.chdir("./images")

url = "https://i.pinimg.com/originals/83/f9/37/83f937b69f30bb886ab8a03390da6771.jpg"
page = requests.get(url)

f_ext = os.path.splitext(url)[-1]
f_name = "img{}".format(f_ext)
with open(f_name, "wb") as f:
    f.write(page.content)
