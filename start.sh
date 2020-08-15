#!/bin/bash
export FLASK_APP=f_test.py
export FLASK_ENV=development
# will save the prints from the
# flask app to a .log file↓
flask run > "log_files/flask_run$(date).log"