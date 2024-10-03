#! /bin/bash

echo "build VODML"
python -m processVodml

echo "build MIVOT snippets"
[ -e ../mivot/mango ] && rm -rf ../mivot/mango

which mivot-snippet-model
if [[ $? -eq 0 ]]; then
	cp ../vo-dml/desc.mango.vo-dml.xml ./mango.vo-dml.xml
	mivot-snippet-model file://`pwd`/mango.vo-dml.xml `pwd`/../mivot/
	rm ./mango.vo-dml.xml
else
	echo "mivot-snippet-model not found: have you 'pip install mivot-validator'"
fi
exit 1
cd ../doc
echo "compile latex"
rm *.aux
make forcetex


cd ../utils


