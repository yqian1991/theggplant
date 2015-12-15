# The Eggplant

## Start the service

```
python setup.py develop
pserve developmen.ini --reload
```

## Sync Data
When models are added or updated, we need to sync database with the changes.
We should do the following.
```
`rm theggplant.sqlite`
initialize_theggplant_db development.ini
```
To add fixtures to the Database, we can modify `theggplant/scripts/initializedb.py`.


### Translation with i18n
To add i18n support for jinja2 templates, we should
`nano ~/.config/lingua.cfg`

In the file, enter
```
[extension:.jinja2]
plugin = babel-jinja2
```
Then we do the following to pick the new translatable text.
```
python setup.py extract_messages
python setup.py update_catalog
```

## Code Structure

### app/account
The web app with login user goes here

### app/api
Restful API for all resources (models and views)

### app/auth
The authenication and authorization goes here

### app/templates
Global templates are here

### app/upload
Image upload API is here

### app/db.py
DB session and base models are here

### app/i18n.py
Translation related sufff

### app/utils.py
Utility functions and wrappers
