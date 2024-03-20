#!/usr/bin/bash

cd  ~/OPI_Lab2/
git init git
cd git

git config --local user.name "RedUser"
git config --local user.email "reduser@niuitmo.ru"

cp -r ../commit0/* .
git add .
git commit -m "r0"

git checkout -b branch1
cp -r ../commit1/* .
git add .
git commit -m "r1"

git checkout -b branch2
cp -r ../commit2/* .
git add .
git commit -m "r2"

git checkout -b branch3
cp -r ../commit3/* .
git add .
git commit -m "r3"

git checkout -b branch4
cp -r ../commit4/* .
git add .
git commit -m "r4" 

git config --local user.name "BlueUser"
git config --local user.email "blueuser@niuitmo.ru"

git checkout -b branch5
cp -r ../commit5/* .
git add .
git commit -m "r5" 

cp -r ../commit6/* .
git add .
git commit -m "r6"

git config --local user.name "RedUser"
git config --local user.email "reduser@niuitmo.ru"

git checkout -b branch6
cp -r ../commit7/* .
git add .
git commit -m "r7"

git checkout branch3
cp -r ../commit8/* .
git add .
git commit -m "r8"

git checkout -b branch7
cp -r ../commit9/* .
git add .
git commit -m "r9"

git checkout master
cp -r ../commit10/* .
git add .
git commit -m "r10"

git config --local user.name "BlueUser"
git config --local user.email "blueuser@niuitmo.ru"

git checkout branch5
cp -r ../commit11/* .
git add .
git commit -m "r11"

git config --local user.name "RedUser"
git config --local user.email "reduser@niuitmo.ru"

git checkout branch4
cp -r ../commit12/* .
git add .
git commit -m "r12"

git checkout branch3
git merge -Xours --no-commit branch4

cp -r ../commit13/* .
git add .
git commit -m "r13"

git checkout branch6
git merge -Xours --no-commit branch3

cp -r ../commit14/* .
git add .
git commit -m "r14"

git checkout branch1
cp -r ../commit15/* .
git add .
git commit -m "r15"

git checkout branch5
git merge -Xours --no-commit branch1

git config --local user.name "BlueUser"
git config --local user.email "blueuser@niuitmo.ru"

cp -r ../commit16/* .
git add .
git commit -m "r16"

git config --local user.name "RedUser"
git config --local user.email "reduser@niuitmo.ru"

git checkout master
cp -r ../commit17/* .
git add .
git commit -m "r17"

git config --local user.name "BlueUser"
git config --local user.email "blueuser@niuitmo.ru"

git checkout branch5
cp -r ../commit18/* .
git add .
git commit -m "r18"

cp -r ../commit19/* .
git add .
git commit -m "r19"

git config --local user.name "RedUser"
git config --local user.email "reduser@niuitmo.ru"

git checkout branch6
cp -r ../commit20/* .
git add .
git commit -m "r20"

git checkout branch2
cp -r ../commit21/* .
git add .
git commit -m "r21"

git checkout -b branch8
cp -r ../commit22/* .
git add .
git commit -m "r22"

git checkout branch7
cp -r ../commit23/* .
git add .
git commit -m "r23"

git checkout branch6
cp -r ../commit24/* .
git add .
git commit -m "r24"

git checkout branch8
git merge -Xours --no-commit branch6

cp -r ../commit25/* .
git add .
git commit -m "r25"

git checkout branch7
cp -r ../commit26/* .
git add .
git commit -m "r26"

git checkout master
git merge -Xours --no-commit branch7

cp -r ../commit27/* .
git add .
git commit -m "r27"

git checkout branch2
cp -r ../commit28/* .
git add .
git commit -m "r28"

git checkout branch8
git merge -Xours --no-commit branch2

cp -r ../commit29/* .
git add .
git commit -m "r29"

git checkout master
cp -r ../commit30/* .
git add .
git commit -m "r30"

git checkout branch8
cp -r ../commit31/* .
git add .
git commit -m "r31"

git checkout master
git merge -Xours --no-commit branch8

cp -r ../commit32/* .
git add .
git commit -m "r32"

git config --local user.name "BlueUser"
git config --local user.email "blueuser@niuitmo.ru"

git checkout branch5
cp -r ../commit33/* .
git add .
git commit -m "r33"

git checkout master
git merge -Xours --no-commit branch5

git config --local user.name "RedUser"
git config --local user.email "reduser@niuitmo.ru"

cp -r ../commit34/* .
git add .
git commit -m "r34"
