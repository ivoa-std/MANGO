#
# INsdert images and model element descriptions in the vo-dml file
# - input:  mango.vodml.xml
# - desc folder: contains all individual model element descriptions
# - output: desc/mango.vodml.xml 
#
# Must be run from that folder
#
import sys, os, re, subprocess
import xml.etree.ElementTree as ET
from datetime import datetime

base_path = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
vodml_path = os.path.join(base_path, "vo-dml")
desc_path = os.path.join(vodml_path, "desc")
doc_path = os.path.join(base_path, "doc")
vodml_model_path = os.path.join(vodml_path, "mango.vo-dml.xml")
tex_model_path = os.path.join(doc_path, "model.tex")

# Image insertion pattern
image = r"""\1 \2 }
  \\begin{figure}[h]
    \\includegraphics[width=1.0\\textwidth]{../model/\2.png}
    \\caption{package \2}
    \\label{fig:\2}
  \\end{figure}\n
"""

# Class for which an image is available
class_with_image = ["EpochPosition"]

def insert_class_image(class_name, content):
    template_class_image = r"""\1\n
      \\begin{figure}[h]
        \\includegraphics[width=1.0\\textwidth]{../model/@@@@.png}
        \\caption{Class @@@@}
        \\label{fig:@@@@}
      \\end{figure}\n
    """
    
    # build a regexp locating that particular image
    regexp = "(section\{@@@@\})".replace("@@@@",class_name)
    
    # insert the latex image block
    return re.sub(regexp,
                  template_class_image.replace("@@@@",class_name), content)



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
        
    with open(tex_model_path, "w") as write_file:
        write_file.write(content)
        
def add_images():
    """
    escape undescores in text, un-escape in formula (indices)
    """
    content = ""
    with open(tex_model_path) as read_file:
        content = read_file.read()
    # add images for each package (image MUST be available
    content = re.sub("(section\{Package:) ([a-z_]+) \}", image, content)
    
    # add images for the class declared as having a diagram
    for class_name in class_with_image:
        content = insert_class_image(class_name, content)
        
    with open(tex_model_path, "w") as write_file:
        write_file.write(content)

def set_date():
    """ set the Makefile date """
    current_date = datetime.now()
    isodate = current_date.strftime('%Y-%m-%d')
    make_path = os.path.join(doc_path, "Makefile")
    content = ""
    with open(make_path) as read_file:
        content = read_file.read()

    content = re.sub("(DOCDATE =) [0-9\-]+", f"\\1 {isodate}", content)

    with open(make_path, "w") as write_file:
        write_file.write(content)
     
def main():
    print("======= Insert model element descriptions in the VO-DML file")
    insert_desc()
    print("======= Translate the VO-DML file into a Tex file")
    vodml_to_tex()
    print("======= escape and un-escape underscores")
    escape_underscores()
    print("======= add images")
    add_images()
    print("======= set date")
    set_date()
    
if __name__ == "__main__":
    main()
