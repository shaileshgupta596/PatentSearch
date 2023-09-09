"""
#######################Python Module for all Transaction with Elastic Search #############################
function : load_all_data : Run at Initial level to Upload all json file to Elastic search
function : get_result : This function will take an argument and return respective responses
function : delete_all_document : This Function will delete all document stored at elastic search
"""

import json
import os
import concurrent.futures
import requests
from requests.auth import HTTPBasicAuth
from app.credential import username, password
from app.query_preparator import get_prepared_query

# Url String
url = 'https://473dca99cb954fdf8234a453ce2179cc.us-central1.gcp.cloud.es.io:443/search-patentsearch/'
# Authentication String for elastic
auth = HTTPBasicAuth(username, password)
# Defining content type for request methods
header = {
        'Content-Type': 'application/json; charset=utf8'
        }


def upload_document(file_name):
    result = ""
    with open('patent_jsons/patent_jsons/' + file_name, 'r') as reader:
        data = reader.read()
    json_data = json.loads(data)  # Converting json to Python Dictionary
    try:
        # Using Put method uploading all data to elastic
        response = requests.put(url='{}_doc/{}'.format(url, json_data['patent_number']),
                                auth=auth,
                                json=json_data,
                                headers=header)
        response = response.json()
        result = '{} -> {}'.format(json_data['patent_number'], response['result'])
    except Exception as e:
        print(e)
        result = "Error while Uploading data for {}".format(json_data['patent_number'])

    return result


def load_all_data():
    file_count = 0
    files = os.listdir('patent_jsons/patent_jsons/')  # Loading all file name which needs to be stored in elastic

    # Using multi-threading to make execution faster : As this Mostly related to IO and Request Operation
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(upload_document, files)

    # count of all files
    for f in results:
        file_count += 1

    print("Number of Document Processed {} ".format(file_count))


def delete_all_document():
    try:
        json_data = {
            "query": {
                "match_all": {}
            }
        }
        response = requests.post(url='{}_delete_by_query'.format(url),
                                 auth=auth,
                                 json=json_data,
                                 headers=header)
        response = response.json()
        print(response)
    except Exception as e:
        print(e)


def get_result(keyword):
    response = {}
    document_names = []
    try:
        query = get_prepared_query(keyword)
        # print(query)
        response = requests.get(url='{}_search'.format(url),
                                auth=auth,
                                json=query,
                                headers=header)
        response = response.json()

        document_count = response['hits']['total']['value']  # Deriving Document Count
        all_document = response['hits']['hits']  # all Matching Documents
        document_names = [i['_id'] for i in all_document]

        # Preparing Response
        response = {
            "Number of Document Matched": document_count,
            "Top 20 documents Name": document_names
        }
    except Exception as e:
        print(e)
    return response
