# Generating the model doc from the VODML


This utility automate as much as possible the transalation of the VODML 
file into a documented Tex file which is inserted into the main Tex file

The process is 3 steps:
- `mango.vo-dml.xml` to `desc.mango.vo-dml.xml` 
  - insert the descriptions located in `vo-dml/desc`intio the vo-dml file
  - description of model elements are like `desc.vodmlid.txt`
  - missing description files are printed out; they can be edited by hand.
  
- `desc.mango.vo-dml.xml` to `doc/model.tex` 
  - XSLT transform
  - style sheet `ivoatex/vo-dml2ivoatex.xslt`

- Uderscore escaping
  - Escape underscores located in the text 
  - Un-Escape underscores located in formula 


```bash
% python -m processVodml
% cd ../doc
% make forcetex
```
