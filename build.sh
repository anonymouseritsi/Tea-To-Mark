#!/bin/bash
python manage.py migrate
python init_data.py