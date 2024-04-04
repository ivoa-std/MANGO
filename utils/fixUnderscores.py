import sys, os, re, subprocess
import xml.etree.ElementTree as ET

base_path = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
vodml_path = os.path.join(base_path, "vo-dml")
doc_path = os.path.join(base_path, "doc")
model_path = os.path.join(doc_path, "model.tex")

#xsltproc -o model.tex  ivoatex/vo-dml2ivoatex.xslt ../vo-dml/desc.mango.vo-dml.xml

subprocess.run(["xsltproc",
                "-o", model_path,
                os.path.join(doc_path, "ivoatex", "vo-dml2ivoatex.xslt"),
                os.path.join(vodml_path, "desc.mango.vo-dml.xml")
                ])


content = ""
with open(model_path) as read_file:
    content = read_file.read()

content = "qqqq_xxxx\nsssss_xxxxx\n\\sigma\n$M\\_B - M\\_v$\nShapeFrame.STC_S\n$(x\\_{11})$\nDataOrigin.reference_url"
content = re.sub('([a-zC])_([a-zS])', r'\1\\_\2', content)
content = content.replace('\\sigma', '$\\sigma$')
content = re.sub('([A-Z])\\\_([^S])', r'\1_\2', content)
content = re.sub('(x)\\\_([{0-9])', r'\1_\2', content)

print(content)
#print("STC_S".replace("_", r"\_"))
#print(re.sub('([a-zC])_([a-zS])', r'\1\\_\2', "sssss_xxxxx\n\\sigma\n$M\\_B - M\\_v$\nShapeFrame.STC_S"))
sys.exit(1)
with open(model_path, "w") as write_file:
    write_file.write(content)
