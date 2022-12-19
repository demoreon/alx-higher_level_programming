#! /bin/bash
mv main.h main.h
echo "A read me file" > README.md
find ./ -type f -exec sed -i -e 's/main/main/g' {} \;
find ./ -type f -exec sed -i -e 's/ALX/ALX/g' {} \;
