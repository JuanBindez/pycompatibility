#!/bin/bash

git add .
git commit -m 'update'
git push -u origin main
git tag v1.0-a2
git push --tag
make clean
make upload