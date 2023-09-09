from flask_restful import Resource
from flask import request
from app.elastic_connections import get_result


class KWBS(Resource):
    """ API for Keyword based Search"""
    def get(self, *args, **kwargs):
        keyword = request.args.get('keyword')
        if keyword is None or keyword == '':  # Validation of url keyword data
            return {"response": "keyword not found",
                    "guide": "please make a request in this format : http://localhost:5000/search/?keyword=helloword"}, 404
        # logic to write keyword based search engine
        response = get_result(keyword)
        return {"response": response}, 200


