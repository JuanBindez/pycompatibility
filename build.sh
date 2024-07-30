#!/bin/bash

git add .
git commit -m 'Pycompatibility 1.0.0 Released'
git push -u origin main
git tag v1.0.0
git push --tag
make clean
make upload