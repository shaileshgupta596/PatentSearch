"""
    *****************************REST API: Patent Search*****************************
    File Structure:
        main.py -> Execution of app Start from Here
        app
            1.__init__.py -> Initialization of app, api, resource done in this file.
            2.credential.py -> Store username, password for Cloud Elastic Search
            3.elastic_connections.py -> All Request Operation with Elastic Cloud Performed .
            4.query_preparator.py -> Preparation of get Query for Elastic Search
            5.views.py -> Contains API Resource -> get Method

    # Features: Will Receive text keyword and return related documents to user
    # Url Example: http://localhost:5000/search/?keyword=helloword
"""
from app import *

app = get_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    # app.run()






