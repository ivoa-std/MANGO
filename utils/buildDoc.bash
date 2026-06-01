#! /bin/bash

echo "----------- build VODML"
python -m processVodml
if [ $? -ne 0 ]; then
  echo "error in processVodml"
  exit 1
fi

echo "----------- Apply custom TOC"
python -m processTOC
if [ $? -ne 0 ]; then
  echo "error in processVodml"
  exit 1
fi
  
echo "build MIVOT snippets"

which mivot-snippet-model
if [[ $? -eq 0 ]]; then
    [ -e ../mivot/mango ] && rm -rf ../mivot/mango
	cp ../vo-dml/desc.mango.vo-dml.xml ./mango.vo-dml.xml
	#mivot-snippet-model file://`pwd`/mango.vo-dml.xml `pwd`/../mivot/
	if [ $? -ne 0 ]; then
		echo "error in snippet building"
  		exit 1
  	fi
	rm ./mango.vo-dml.xml
else
	echo "mivot-snippet-model not found: have you 'pip install mivot-validator'"
fi

cd ../doc
echo "compile latex"
rm *.aux
make forcetex


cd ../utils

