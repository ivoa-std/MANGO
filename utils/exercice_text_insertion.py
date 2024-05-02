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
# This is a test module
#
import sys, os, re
import xml.etree.ElementTree as ET

base_path = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
vodml_path = os.path.join(base_path, "vo-dml")
desc_path = os.path.join(vodml_path, "desc")
model_path = os.path.join(vodml_path, "mango.vo-dml.xml")
tree = ET.parse(model_path)
    
    
root = tree.getroot()
for ele in root.findall(".//vodml-id"):
    vodmlid = ele.text
    desc_ele = root.find(".//vodml-id[.='" + vodmlid + "']/../description")
    description = desc_ele.text

    desc_file = os.path.join(desc_path, ("desc." + vodmlid + ".txt"))
    if not os.path.exists(desc_file):
        print(f"desc file {desc_file} does not exist")
        continue
    with open(desc_file, "r") as read_desc:
        desc = read_desc.read()
        desc_ele.text = desc

tree.write(os.path.join(vodml_path, "desc.mango.vo-dml.xml"))
