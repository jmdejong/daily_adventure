#!/bin/sh

echo "
#ifndef PATHS_H
#define PATHS_H
char basedir[] = \"`pwd`/\";
char inputfname[] = \"`pwd`/data/input/%s.input.txt\";
char infofname[] = \"`pwd`/data/players/%s.json\";
#endif " > paths.h
