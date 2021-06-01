import pandas as pd
from flask import Flask, jsonify, request
import pickle
from swagger.app import blueprint as app_endpoints


# load model
model = pickle.load(open('models/model.pkl','rb'))

# app
app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False
app.register_blueprint(app_endpoints)

# routes
@app.route('/prediction', methods=['GET', 'POST'])

def predict():

    if request.method == "GET":
        return {
            'message': 'This endpoint should return past predictions',
            'method': request.method
        }
    
    if request.method == "POST":
        
        # get data
        data = request.get_json(force=True)

        # convert data into dataframe
        data.update((x, [y]) for x, y in data.items())
        data_df = pd.DataFrame.from_dict(data)

        # predictions
        result = model.predict(data_df)

        # send back to browser
        output = {'results': int(result[0])}

        # return data
        return jsonify(results=output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True, host='0.0.0.0')