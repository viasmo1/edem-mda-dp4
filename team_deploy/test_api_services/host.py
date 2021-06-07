import base64
import requests
import datetime

def get_method():
    r = requests.get('http://127.0.0.1:5000/prediction')
    print(r.text)

def return_json(str_name, str_img):
    return '{"creationDate":'+'"'+str_name+'"'+','+'"message":'+'"'+str_img+'"'+'}'
 
def post_method():
    with open('presi.jpg', 'rb') as binary_file:
            binary_file_data = binary_file.read()
            base64_encoded_data = base64.b64encode(binary_file_data)
            base64_message = base64_encoded_data.decode('utf-8')

    
    creationDate = str(datetime.datetime.now())
    data_in = return_json(creationDate, base64_message)
    #data_in = return_json_val()
    print(data_in)
    r = requests.post("http://127.0.0.1:5000/prediction", data=data_in)
    print(r.text)

post_method()