#!/bin/bash

git add .
git commit -m 'update'
git push -u origin Release_Candidate
git tag v1.0-rc3
git push --tag
make clean
make upload