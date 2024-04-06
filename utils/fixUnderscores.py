#
# Test module for regular expressions
#
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

image = r"""\1 \2 }
  \\begin{figure}[h]
  \\begin{center}
    \\includegraphics\[width=textwidth]{../model/\2.png}
    \\caption{\2}
    \\label{fig:\2}
  \\end{package \2}
  \\end{figure}\n
"""
content = "qqqq_xxxx\nsssss_xxxxx\n\\sigma\n$M\\_B - M\\_v$\nShapeFrame.STC_S\n$(x\\_{11})$\nDataOrigin.reference_url"
content = "\\section{Package: correlation }\n"
print(content)
content = re.sub("(section\{Package:) ([a-z_]+) \}", image, content)

print(content)
#print("STC_S".replace("_", r"\_"))
#print(re.sub('([a-zC])_([a-zS])', r'\1\\_\2', "sssss_xxxxx\n\\sigma\n$M\\_B - M\\_v$\nShapeFrame.STC_S"))
sys.exit(1)
with open(model_path, "w") as write_file:
    write_file.write(content)
