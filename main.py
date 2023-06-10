def convert_yaml_to_json(file_path, output_path):
    with open(file_path) as yaml_file:
        data = yaml.safe_load(yaml_file)
    with open(output_path, 'w') as outfile:
        json.dump(data, outfile)
