#!/usr/bin/bash

cd  ~/OPI_Lab2/
svnadmin create svn

cd svn
location="$HOME/OPI_Lab2/svn/"

svn mkdir -m “structure” "file:///$location/trunk" "file:///$location/branches" --username RedUser
svn checkout "file:///$location/trunk" mainDir
cd mainDir

cp -r ../../commit0/* .
svn add *
svn commit -m "r0" --username RedUser

svn copy "file:///$location/trunk" "file:///$location/branches/branch1" -m "branch1" --username RedUser
svn switch "file:///$location/branches/branch1"
cp -r ../../commit1/* .
svn add --force .
svn commit -m "r1" --username RedUser

svn copy "file:///$location/branches/branch1" "file:///$location/branches/branch2" -m "branch2" --username RedUser
svn switch "file:///$location/branches/branch2"
cp -r ../../commit2/* .
svn add --force .
svn commit -m "r2" --username RedUser

svn copy "file:///$location/branches/branch2" "file:///$location/branches/branch3" -m "branch3" --username RedUser
svn switch "file:///$location/branches/branch3"
cp -r ../../commit3/* .
svn add --force .
svn commit -m "r3" --username RedUser

svn copy "file:///$location/branches/branch3" "file:///$location/branches/branch4" -m "branch4" --username RedUser
svn switch "file:///$location/branches/branch4"
cp -r ../../commit4/* .
svn add --force .
svn commit -m "r4" --username RedUser

svn copy "file:///$location/branches/branch4" "file:///$location/branches/branch5" -m "branch5" --username BlueUser
svn switch "file:///$location/branches/branch5"
cp -r ../../commit5/* .
svn add --force .
svn commit -m "r5" --username BlueUser

cp -r ../../commit6/* .
svn add --force .
svn commit -m "r6" --username BlueUser

svn copy "file:///$location/branches/branch5" "file:///$location/branches/branch6" -m "branch6" --username RedUser
svn switch "file:///$location/branches/branch6"
cp -r ../../commit7/* .
svn add --force .
svn commit -m "r7" --username RedUser

svn switch "file:///$location/branches/branch3"
cp -r ../../commit8/* .
svn add --force .
svn commit -m "r8" --username RedUser

svn copy "file:///$location/branches/branch3" "file:///$location/branches/branch7" -m "branch7" --username RedUser
svn switch "file:///$location/branches/branch7"
cp -r ../../commit9/* .
svn add --force .
svn commit -m "r9" --username RedUser

svn switch "file:///$location/trunk"
cp -r ../../commit10/* .
svn add --force .
svn commit -m "r10" --username RedUser

svn switch "file:///$location/branches/branch5"
cp -r ../../commit11/* .
svn add --force .
svn commit -m "r11" --username BlueUser

svn switch "file:///$location/branches/branch4"
cp -r ../../commit12/* .
svn add --force .
svn commit -m "r12" --username RedUser

svn switch "file:///$location/branches/branch3"
svn merge --accept mine-full "file:///$location/branches/branch4"
svn commit -m "Merged branch4 into branch3" --username RedUser

cp -r ../../commit13/* .
svn add --force .
svn commit -m "r13" --username RedUser

svn switch "file:///$location/branches/branch6"
svn merge --accept mine-full "file:///$location/branches/branch3"
svn commit -m "Merged branch3 into branch6" --username RedUser

cp -r ../../commit14/* .
svn add --force .
svn commit -m "r14" --username RedUser

svn switch "file:///$location/branches/branch1"
cp -r ../../commit15/* .
svn add --force .
svn commit -m "r15" --username RedUser

svn switch "file:///$location/branches/branch5"
svn merge --accept mine-full "file:///$location/branches/branch1"
svn commit -m "Merged branch1 into branch5" --username RedUser

cp -r ../../commit16/* .
svn add --force .
svn commit -m "r16" --username BlueUser

svn switch "file:///$location/trunk"
cp -r ../../commit17/* .
svn add --force .
svn commit -m "r17" --username RedUser

svn switch "file:///$location/branches/branch5"
cp -r ../../commit18/* .
svn add --force .
svn commit -m "r18" --username BlueUser

cp -r ../../commit19/* .
svn add --force .
svn commit -m "r19" --username BlueUser

svn switch "file:///$location/branches/branch6"
cp -r ../../commit20/* .
svn add --force .
svn commit -m "r20" --username RedUser

svn switch "file:///$location/branches/branch2"
cp -r ../../commit21/* .
svn add --force .
svn commit -m "r21" --username RedUser

svn copy "file:///$location/branches/branch2" "file:///$location/branches/branch8" -m "branch8" --username RedUser
svn switch "file:///$location/branches/branch8"
cp -r ../../commit22/* .
svn add --force .
svn commit -m "r22" --username RedUser

svn switch "file:///$location/branches/branch7"
cp -r ../../commit23/* .
svn add --force .
svn commit -m "r23" --username RedUser

svn switch "file:///$location/branches/branch6"
cp -r ../../commit24/* .
svn add --force .
svn commit -m "r24" --username RedUser

svn switch "file:///$location/branches/branch8"
svn merge --accept mine-full "file:///$location/branches/branch6"
svn commit -m "Merged branch6 into branch8" --username RedUser

cp -r ../../commit25/* .
svn add --force .
svn commit -m "r25" --username RedUser

svn switch "file:///$location/branches/branch7"
cp -r ../../commit26/* .
svn add --force .
svn commit -m "r26" --username RedUser

svn switch "file:///$location/trunk"
svn merge --accept mine-full "file:///$location/branches/branch7"
svn resolve --accept working -R .
svn merge --accept mine-full "file:///$location/branches/branch7"
svn commit -m "Merged branch7 into trunk" --username RedUser

cp -r ../../commit27/* .
svn add --force .
svn commit -m "r27" --username RedUser

svn switch "file:///$location/branches/branch2"
cp -r ../../commit28/* .
svn add --force .
svn commit -m "r28" --username RedUser

svn switch "file:///$location/branches/branch8"
svn merge --accept mine-full "file:///$location/branches/branch2"
svn commit -m "Merged branch2 into branch8" --username RedUser

cp -r ../../commit29/* .
svn add --force .
svn commit -m "r29" --username RedUser

svn switch "file:///$location/trunk"
cp -r ../../commit30/* .
svn add --force .
svn commit -m "r30" --username RedUser

svn switch "file:///$location/branches/branch8"
cp -r ../../commit31/* .
svn add --force .
svn commit -m "r31" --username RedUser

svn switch "file:///$location/trunk"
svn merge --accept mine-full "file:///$location/branches/branch8"
svn commit -m "Merged branch8 into trunk" --username RedUser

cp -r ../../commit32/* .
svn add --force .
svn commit -m "r32" --username RedUser

svn switch "file:///$location/branches/branch5"
cp -r ../../commit33/* .
svn add --force .
svn commit -m "r33" --username BlueUser

svn switch "file:///$location/trunk"
svn merge --accept mine-full "file:///$location/branches/branch5"
svn commit -m "Merged branch5 into trunk" --username BlueUser

cp -r ../../commit34/* .
svn add --force .
svn commit -m "r34" --username RedUser
