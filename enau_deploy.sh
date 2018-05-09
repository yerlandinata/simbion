#!/bin/bash

folder="${PWD##*/}";
cd ..;
ls -la;
tar -czf ${CIRCLE_SHA1}.tar.gz $folder;
ls -la;
scp ${CIRCLE_SHA1}.tar.gz yudhistira.erlandinata@kawung.cs.ui.ac.id;
ssh yudhistira.erlandinata@kawung.cs.ui.ac.id "
    scp ${CIRCLE_SHA1}.tar.gz enau.cs.ui.ac.id;
    ssh enau.cs.ui.ac.id '
        source resetweb.sh;
        mv ${CIRCLE_SHA1}.tar.gz web/;
        cd web;
        tar -xzf ${CIRCLE_SHA1}.tar.gz;
        python3 -m virtualenv env; source env/bin/activate;
        cd $folder;
        pip install -r requirements.txt;
        gunicorn -b 0.0.0.0:8020 simbion.wsgi & sleep 5;
    '
";
