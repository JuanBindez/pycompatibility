#!/bin/bash

git add .
git commit -m 'update merge -> Alfa -> Release_Candidate'
git push -u origin Release_Candidate
git tag v1.0-rc1
git push --tag
make clean
make upload