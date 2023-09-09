# importing Required Module
from flask import Flask
from flask_restful import Api
from app.elastic_connections import delete_all_document, load_all_data


def get_app():
    # Initialization of Flask App
    app = Flask(__name__)
    # Configured Secret : As is it not needed for this Application because it has only get Request method
    # app.config['SECRET_KEY'] = "jdbfjbkdfkdrivivhfvhjahvjhvajvqwdjshvdjhsvdjhshkf"
    # Initialization of Api
    api = Api(app)

    # Deleting All data
    # print("Deleting all Data from Elastic Search .................")
    # delete_all_document()
    # Uploading all Data
    # print("Re-uploading  all Data to Elastic Search ... Please wait for few Seconds")
    # load_all_data()

    from app.views import KWBS

    # Register Resource to API
    api.add_resource(KWBS, '/search/')  # Register Resource in API and setup endpoint

    return app



