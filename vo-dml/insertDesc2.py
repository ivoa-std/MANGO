#
#
# scan mango.vo-dml.xml file
# - extract all @xyz@ pattern
# - replace the with the content of the file named ./desc/desc.xxyz/txt
# - save the result in desc.mango.vo-dml.xml
#
# Before doing the replacement, the script verifies that all referenced files really exit
# Exit on error if not
#
import sys, os, re
import xml.etree.ElementTree as ET

base_path = os.path.realpath(os.path.join(os.path.dirname(__file__), "../vo-dml/"))
vodml_path = os.path.join(base_path, "mango.vo-dml.xml")
tree = ET.parse(vodml_path)
    
    
root = tree.getroot()
for ele in root.findall(".//vodml-id"):
    vodmlid = ele.text
    desc_ele = root.find(".//vodml-id[.='" + vodmlid + "']/../description")
    description = desc_ele.text
    if True or "TODO" in description:
        desc_file = os.path.join(base_path, "desc", ("desc." + vodmlid + ".txt"))
        if not os.path.exists(desc_file):
            print(f"desc file {desc_file} does not exist")
            continue
        with open(os.path.join(base_path, "desc", ("desc." + vodmlid + ".txt")), "r") as read_desc:
            desc = read_desc.read()
            desc_ele.text = desc

tree.write(os.path.join(base_path, "desc.mango.vo-dml.xml"))
