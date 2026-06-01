#
# Rearrange model.tex by applying the input toc.json
# - input:  doc/model.text (generated from VODML)
# - input:  toc.json: table of content to be applied
# - output: doc/model_ordered.tex Text file ready to be compiled 
#
# Must be run from that folder
#
import os, re, json

base_path = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
doc_path = os.path.join(base_path, "doc")
tex_model_path = os.path.join(doc_path, "model.tex")
tex_omodel_path = os.path.join(doc_path, "model_toc.tex")
toc_path = os.path.realpath(os.path.join(os.path.dirname(__file__), "toc.json"))
toc_org_path = os.path.realpath(os.path.join(os.path.dirname(__file__), "toc.org.json"))
vodml_path = os.path.join(base_path, "vo-dml")
desc_path = os.path.join(vodml_path, "sections")

def format_enum(text):
    """
    The original XSLT writes enum literals out of the box
    This feature is override  here. 
    """
    print("Push enum literals back in the box")
    formatted_text = ""
    pattern = r"\\item\[(.*)\]"
    replacement = r"\\item \1"
    formatted_text = (re.sub(pattern, replacement, text))
    return formatted_text.replace("\\noindent \\underline", "\\newline \\newline \\noindent \\underline")

def extract_title(string):
    """
    return the (sub)section title extracted from the Latex tag
    """
    return re.search(r"\{(.*)\}", string).group(1).strip() 

def get_custom_content(searched_title):
    """
    extract the content of a (sub)section from a custom description if it exists
    """
    doc_title = searched_title.replace("(added)", "").strip().replace(" ", "_")
    txt_path = os.path.join(desc_path, f"{doc_title}.txt")
    if os.path.isfile(txt_path):
        print(f"FOUND SECTION  head file {txt_path}")
        with open(txt_path)  as file_reader:
            return file_reader.read()
    else:
        print(f"SECTION  head file {txt_path} not found: skip")
    return ""
    
def get_content(searched_title):
    """
    extract the content of a (sub)section out of the original document 
    or from a custom description
    """
    if ("added" in searched_title):
        return get_custom_content(searched_title)
    started = False
    current_content = ""
    with open(tex_model_path) as tmp:
        while (line := tmp.readline()):
            line = line.strip()
            if not line or line.startswith("%") or line.startswith("\\page"):
                continue
            if line.startswith("\\section") or line.startswith("\\subsection"):
                if started:
                    return current_content 
                if (title := extract_title(line)) == searched_title:
                    started = True
            elif started:
                if "subsub" in line:
                    current_content += "\n"
                current_content += f"    {line}\n"
                
        
        return current_content
    
def save_current_toc(): 
    """
    Print out the ToC of the current document
    """
    toc = {}
    with open(tex_model_path) as tmp:
        while (line := tmp.readline()):
            line = line.strip()
            if not line or line.startswith("%") or line.startswith("\\page"):
                continue
            if line.startswith("\\section"):
                title = extract_title(line)
                toc[title] = {"content": "", "subsections": {}}
                current_section = toc[title]["subsections"]
            if line.startswith("\\subsection"):
                title = extract_title(line)
                current_section[title] = {"content": ""}
    with open(toc_org_path, "w") as writer:
        print(f"Save the original TOC in {toc_org_path}")
        writer.write(json.dumps(toc))

def main():
    """
    do the job
    """
    
    toc = None
    new_text = "\\pagebreak\n\n"

    save_current_toc()    
    # read the new ToC
    print(f"Read custom ToC from {toc_path}")
    
    if not os.path.isfile(toc_path):
        print("No custom TOC")
        shutil.copy(tex_model_path, tex_omodel_path)
        sys.exit(0)
        
    with open(toc_path) as toc_file:
        toc = json.loads(toc_file.read())
        
    # build in memory the new doc (sub)section by section
    print(f"Extract (sub)sections from {tex_model_path}")
    for section, content in toc.items():
        new_text += "\\section{" + section.replace("(added)", "").strip() + "}\n"
        new_text += get_content(section.strip()) + "\n"
        for subsection, _ in content.items():
            new_text += "  \\subsection{" + subsection + "}\n"
            new_text += get_content(subsection.strip()) + "\n"

    new_text = format_enum(new_text)
    # save the new document
    print(f"Write rearranged document in {tex_omodel_path}")
    with open(tex_omodel_path, "w") as output:
        output.write(new_text)

if __name__ == "__main__":
    main()
