#!/bin/bash

git add .
git commit -m 'update'
git push -u origin Alfa
git tag v1.0-a7
git push --tag
make clean
make upload