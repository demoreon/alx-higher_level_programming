#! /bin/bash
echo "A read me file" > README.md
git add .
git commit -m $1
git push
