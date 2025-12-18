# Generating the model doc from the VODML

This utility automate as much as possible the transalation of the VODML 
file into a documented Tex file which is inserted into the main Tex file

The process is 3 steps:
- `mango.vo-dml.xml` to `desc.mango.vo-dml.xml` 
  - insert the descriptions located in `vo-dml/desc`into the vo-dml file
  - description of model elements are like `desc.vodmlid.txt`
  - missing description files are printed out; they can be edited by hand.
  
- `desc.mango.vo-dml.xml` to `doc/model.tex` 
  - XSLT transform
  - style sheet `ivoatex/vo-dml2ivoatex.xslt`

- apply the custom TOC from `toc.json`
  - edit the custom toc (new section must contain the `(added)` word
  - The TEX document is rebuilt following that TOC
  - The head text of the added section is in `vo-dml/sections`
  - The final TEX file is named model_toc.tex `model_toc.tex`
  
```bash
% ./builDoc.bash
```

# Flow Chart

<img width="865" alt="Screenshot 2025-06-19 at 15 29 06" src="https://github.com/user-attachments/assets/cc32dc81-adfa-46f8-9b20-c6b970f5a73d" />
