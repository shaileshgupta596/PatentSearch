"""
############################ Module : query ###################################
    Description : based upon keyword data type Generating json Query which will be used to perform search
    function : is_date : check keyword is date or not
    function : is_integer : check keyword is integer or not
    function : get_prepared_query to generate Query

"""

from datetime import datetime


def is_date(keyword):
    date_format = "%Y-%m-%d"
    result = True
    try:
        result = bool(datetime.strptime(keyword, date_format))
    except ValueError:
        result = False
    return result


def is_integer(keyword):
    return keyword.isnumeric()


def get_prepared_query(keyword):
    keyword = keyword.strip()
    json_query = {}
    print(keyword)
    if is_date(keyword):
        print("String is Date")
        json_query = {
            "size": 20,
            "query": {
                "multi_match": {
                    "query": keyword,
                    "fields": ["publication_date", "priority_date", "application_date"],
                    "type": "phrase"
                }
            }
        }
    elif is_integer(keyword):
        print("String is Number")
        json_query = {
            "size": 20,
            "query": {
                "multi_match": {
                    "query": keyword,
                    "fields": ["publication_id", "family_id"],
                    "type": "phrase"
                }
            }
        }
    else:
        print("String is String")
        json_query = {
            "size": 20,
            "query": {
                "multi_match": {
                    "query": keyword,
                    "fields": ["patent_number",
                               "titles.text",
                               "abstracts.paragraph_markup",
                               "claims.claim.paragraph_markup",
                               "claims.claims.type",
                               "descriptions.paragraph_markup",
                               "inventors.first_name",
                               "inventors.last_name",
                               "inventors.name",
                               "assignees.first_name",
                               "assignees.last_name",
                               "assignees.name",
                               "ipc_classes.label",
                               "ipcr_classes.label",
                               "national_classes.label",
                               "ecla_classes.label",
                               "cpc_classes.label",
                               "family_members.ucid",
                               "family_members.titles.text",
                               "legal_status"],
                    "type": "phrase"
                }
            }
        }

    return json_query

