#
#
#
import sys, os, re, subprocess
import xml.etree.ElementTree as ET

base_path = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
vodml_path = os.path.join(base_path, "vo-dml")
desc_path = os.path.join(vodml_path, "desc")
doc_path = os.path.join(base_path, "doc")
vodml_model_path = os.path.join(vodml_path, "mango.vo-dml.xml")
tex_model_path = os.path.join(doc_path, "model.tex")

image = r"""\1 \2 }
  \\begin{figure}[h]
    \\includegraphics[width=1.0\\textwidth]{../model/\2.png}
    \\caption{package \2}
    \\label{fig:\2}
  \\end{figure}\n
"""
    
def insert_desc():    
    tree = ET.parse(vodml_model_path)
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

def vodml_to_tex():
    subprocess.run(["xsltproc",
                "-o", tex_model_path,
                os.path.join(doc_path, "ivoatex", "vo-dml2ivoatex.xslt"),
                os.path.join(vodml_path, "desc.mango.vo-dml.xml")
                ])
def escape_underscores():
    """
    escape undescores in text, un-escape in formula (indices)
    """
    content = ""
    with open(tex_model_path) as read_file:
        content = read_file.read()
    
    content = re.sub('([a-zC])_([a-zS])', r'\1\\_\2', content)
    content = re.sub('([A-Z])\\\_([^S])', r'\1_\2', content)
    content = re.sub('(x)\\\_({[0-9])', r'\1_\2', content)
    content = re.sub("(section\{Package:) ([a-z_]+) \}", image, content)

    with open(tex_model_path, "w") as write_file:
        write_file.write(content)

def main():
    print("======= Insert model element descriptions in the VO-DML file")
    insert_desc()
    print("======= Translate the VO-DML file into a Tex file")
    vodml_to_tex()
    print("======= escape and un-escape underscores")
    escape_underscores()
    
if __name__ == "__main__":
    main()
