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
