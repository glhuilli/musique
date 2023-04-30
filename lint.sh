#!/usr/bin/env bash

mypy musique/
pylint -j 4 --rcfile=.pylintrc musique/*
yapf -vv -pri ./musique

