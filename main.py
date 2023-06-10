import json

def convert_json_to_xml(file_path, output_path):
    with open(file_path) as json_file:
        data = json.load(json_file)


def convert_json_to_yaml(file_path, output_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
 
