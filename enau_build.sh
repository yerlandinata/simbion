#!/bin/bash

folder="${PWD##*/}";
cd ..;
ls -la;
tar -czf deploy.tar.gz $folder;
ls -la;
mv deploy.tar.gz $folder;
