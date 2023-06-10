def convert_json_to_xml(file_path, output_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
    root = ET.Element("root")
    for key, value in data.items():
        child = ET.SubElement(root, key)
        child.text = value
    tree = ET.ElementTree(root)
    tree.write(output_path)
