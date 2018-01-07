#! /bin/bash

PROJ=$1
abspath=`pwd`
GITBOOK=$abspath/../gitbook/$PROJ
BUILD=$abspath/$PROJ/_book

if [ ! -n "$1" ] || [ ! -d $GITBOOK ]; then
    echo "Usage: ./gitbook.sh bookname"
    exit 1
fi

git pull

if [ -n "$GITBOOK" ]; then
    rm -rf $BUILD/*
    rm -rf $GITBOOK/*
fi
gitbook build $PROJ
mv $BUILD/* $GITBOOK
sync
cd $GITBOOK
git add .
git commit -m "Update $PROJ book"
git push -u origin gh-pages
