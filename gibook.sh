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
gitbook build $PROJ

if [ -n "$GITBOOK" ]; then
    rm -rf $GITBOOK/*
fi

mv $BUILD/* $GITBOOK
cd $GITBOOK
git add .
git commit -m "Update $PROJ book"
git push -u origin gh-pages
