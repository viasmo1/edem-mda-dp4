from flask import Blueprint
from flask_restplus import Api
from swagger.service.prediction import namespace as prediction_ns
#from swagger.service.photo import namespace as photo_ns

blueprint = Blueprint('documented_api', __name__, url_prefix='/documented_api')

api_extension = Api(
    blueprint,
    title='Deployment DP04',
    version='1.0',
    description='Deploy AI model with Flask',
    doc='/doc'
)

api_extension.add_namespace(prediction_ns)
#api_extension.add_namespace(photo_ns)