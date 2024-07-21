#!/bin/bash

git add .
git commit -m 'init pycompatibility'
git push -u origin main
git tag v1.0-a1
git push --tag
make clean
make upload