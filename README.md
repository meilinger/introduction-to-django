# Introduction To Django

A quick and very dirty introduction to Django using a tree location cataloging example web application concept.

_Assumes PostgreSQL + GDAL are installed_

```bash
pip install -r requirements.txt
psql -c "create database treeseeker"
psql treeseeker -c "create extension postgis"
cd treeseeker && python manage.py migrate
python manage.py runserver  # open browser to localhost:8000
```

see [Introduction to Django.ipynb](Introduction to Django.ipynb) for more information
