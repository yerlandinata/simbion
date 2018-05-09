#!/bin/bash

folder="${PWD##*/}";
cd ..;
ls -la;
tar -czf deploy.tar.gz $folder;
ls -la;
mv deploy.tar.gz $folder;
cd $folder;
scp deploy.tar.gz yudhistira.erlandinata@kawung.cs.ui.ac.id;
ssh yudhistira.erlandinata@kawung.cs.ui.ac.id "
    scp deploy.tar.gz enau.cs.ui.ac.id;
    ssh enau.cs.ui.ac.id '
        source resetweb.sh;
        mv deploy.tar.gz web/;
        cd web;
        tar -xzf deploy.tar.gz;
        export all_proxy=\"http://proxy.cs.ui.ac.id:8080/\";
        python3 -m virtualenv env; source env/bin/activate;
        cd $folder;
        pip install -r requirements.txt;
        gunicorn -b 0.0.0.0:8020 simbion.wsgi & sleep 5;
    '
";
