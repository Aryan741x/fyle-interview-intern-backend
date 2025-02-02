from flask import Response, jsonify, make_response


class APIResponse(Response):
    @classmethod
    def respond(cls, data):
        return make_response(jsonify(data=data))
    
    @staticmethod
    def respond_error(error_message, status_code):
        return {
            'error': error_message,
        }, status_code
    def respond_error_submit(error_message, status_code):
        return make_response(jsonify({
            'error': error_message,
            "message": 'only a draft assignment can be submitted'
        }), status_code)
