#!/bin/bash

ssh yudhistira.erlandinata@kawung.cs.ui.ac.id 'rm -rf build_basdat';
scp -r . yudhistira.erlandinata@kawung.cs.ui.ac.id:~/build_basdat;
ssh yudhistira.erlandinata@kawung.cs.ui.ac.id "
    cd build_basdat;
    ssh enau.cs.ui.ac.id '
        rm -rf web/*;
        killall gunicorn;  
    ';
    scp -r . enau.cs.ui.ac.id:~/web;
    ssh enau.cs.ui.ac.id '
        cd web;
        export all_proxy=\"http://proxy.cs.ui.ac.id:8080/\";
        python3 -m virtualenv env; source env/bin/activate;
        pip install -r requirements.txt;
        gunicorn -b 0.0.0.0:8020 simbion.wsgi & sleep 5;
    '
";
