#! /bin/bash

echo "build VODML"
python -m processVodml

echo "build MIVOT snippets"
echo "do not forget 'pip install mivot-validator'"
[ -e ../mivot/mango ] && rm -rf ../mivot/mango
cp ../vo-dml/desc.mango.vo-dml.xml ./mango.vo-dml.xml
mivot-snippet-model file://`pwd`/mango.vo-dml.xml `pwd`/../mivot/

cd ../doc
echo "compile latex"
rm *.aux
make forcetex


cd ../utils


