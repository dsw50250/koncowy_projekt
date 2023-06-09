import sys
import xml.etree.ElementTree as ET
import json
import yaml

def convert_xml_to_json(file_path, output_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = {}
    for child in root:
        data[child.tag] = child.text
    with open(output_path, 'w') as outfile:
        json.dump(data, outfile)

def convert_json_to_xml(file_path, output_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
    root = ET.Element("root")
    for key, value in data.items():
        child = ET.SubElement(root, key)
        child.text = value
    tree = ET.ElementTree(root)
    tree.write(output_path)

def convert_yaml_to_json(file_path, output_path):
    with open(file_path) as yaml_file:
        data = yaml.safe_load(yaml_file)
    with open(output_path, 'w') as outfile:
        json.dump(data, outfile)

def convert_json_to_yaml(file_path, output_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
    with open(output_path, 'w') as outfile:
        yaml.safe_dump(data, outfile)

def convert_files(input_file_path, output_file_path):
    if input_file_path.endswith('.xml') and output_file_path.endswith('.json'):
        convert_xml_to_json(input_file_path, output_file_path)
    elif input_file_path.endswith('.json') and output_file_path.endswith('.xml'):
        convert_json_to_xml(input_file_path, output_file_path)
    elif input_file_path.endswith('.yaml') and output_file_path.endswith('.json'):
        convert_yaml_to_json(input_file_path, output_file_path)
    elif input_file_path.endswith('.json') and output_file_path.endswith('.yaml'):
        convert_json_to_yaml(input_file_path, output_file_path)
    else:
        print("Nieobsługiwany format pliku!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Sposób użycia: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    convert_files(input_file_path, output_file_path)
