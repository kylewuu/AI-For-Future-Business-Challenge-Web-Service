from classes.Apples import *
import json


def get_statuses_all():
    # docker change
    # with open('resources\\temp_db\\data.json') as json_file:
    with open('data.json') as json_file:
        data = json.load(json_file)
        # print(data)
        # return data

        damaged_apples_count = data['damaged_apples_count']
        total_apples_count = data['total_apples_count']
        undamaged_apples_count = total_apples_count - damaged_apples_count

    apples = Apples(total_apples_count, damaged_apples_count)

    return {"total_apples_count": apples.total_apples_count, "damaged_apples_count": apples.damaged_apples_count, "undamaged_apples_count": undamaged_apples_count}
