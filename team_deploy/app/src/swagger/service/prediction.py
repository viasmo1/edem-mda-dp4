from flask import request
from flask_restplus import Namespace, Resource, fields

namespace = Namespace('Prediction', 'Image classifier')

metrics_model = namespace.model('metrics', {
    'accuracy': fields.Float(
        readonly=True,
        description='Model accuracy'
    ),
    'execution_time': fields.Integer(
        readonly=True,
        description='execution time'
    ),
})

prediction_model = namespace.model('prediction', {
    'emotions': fields.String(
        readonly=True,
        description='Array about emotions'
    ),
    'Gender': fields.String(
        readonly=True,
        description='Gender'
    ),
    'Age': fields.Integer(
        readonly=True,
        description='Age'
    ),
    'Race': fields.Integer(
        readonly=True,
        description='Age'
    ),
    'model_metrics': fields.Nested(
        metrics_model,
        readonly=True,
        description='Age',
        as_list=True
    )
})

get_prediction_model = namespace.model('get_prediction', {
    'id': fields.String(
        required=True,
        description='get prediction by ID'
    )
})

@namespace.route('')
class prediction(Resource):

    @namespace.marshal_list_with(prediction_model)
    @namespace.response(500, 'Internal Server error')
    def post(self):
        '''Prediction endpoint'''
        return prediction_model
    @namespace.marshal_list_with(get_prediction_model)
    def get(self):
        '''Prediction endpoint'''
        return get_prediction_model