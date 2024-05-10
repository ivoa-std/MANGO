#! /bin/bash

echo "build VODML"
python -m processVodml

cd ../doc
echo "compile latex"
rm *.aux
make forcetex
cd ../utils
