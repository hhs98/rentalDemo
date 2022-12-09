import json
import os

from django.core.serializers.json import DjangoJSONEncoder


def convert_json_to_fixtures(json_file_path, fixture_file_path):
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    with open(fixture_file_path, 'w') as f:
        pk = 1
        data_list = []
        for item in data:
            dict_item = {'model': 'products.product', 'pk': pk, 'fields': item}
            data_list.append(dict_item)
            pk += 1
        json.dump(data_list, f, cls=DjangoJSONEncoder, indent=4)


if __name__ == '__main__':
    json_file = os.path.join(os.path.dirname(__file__), 'backend-frontend-data.json')
    fixture_file = os.path.join(os.path.dirname(__file__), 'products.json')
    convert_json_to_fixtures(json_file, fixture_file)
