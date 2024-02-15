
import sys, os, re

base_path = os.path.realpath(os.path.join(os.path.dirname(__file__), "../vo-dml/"))
vodml_path = os.path.join(base_path, "mango.vo-dml.xml")

replacement = {}
print(vodml_path)
with open(vodml_path, "r") as vodml:
    for line in vodml.readlines():
        results = re.search(r'(@.*@)', line)
        if results:
            replacement[results.group(1)] = f"desc.{results.group(1).strip('@')}.txt"
    print(replacement)
    
missing = []
for key, value in replacement.items():
    if not os.path.exists(os.path.join(base_path,value)):
        missing.append(value)       
        
if len(missing) > 0:
    print(f"the following description files are missing: {missing}")      
    sys.exit(1)

with open(vodml_path, "r") as read_vodml:
    content = read_vodml.read()
    for key, value in replacement.items():
        with open(os.path.join(base_path,value), "r") as read_desc:
            desc = read_desc.read()
            print(f"insert {value}")
            content = content.replace(key, desc)
            
vodml_desc_path = os.path.join(base_path, "desc.mango.vo-dml.xml")
print(f"write {vodml_desc_path}")
with open(vodml_desc_path, "w") as write_vodml:
    write_vodml.write(content)


