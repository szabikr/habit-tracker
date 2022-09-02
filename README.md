# My Habit Tracker

### Run

```
$ python3 import_activities.py habits_{some_date_range}.txt
```
In order to import activities from user input. This will merge the already existig activities list with the new one and save it to the `data.txt` file (currently this file is considered the database).

```
$ python3 when_did_i_do.py {activity_name}
```
Prints out the records (date, activity name, life aspect) associated with the requested `activity_name`.

### Unit tests

Prerequisites 
```
$ python3 -m venv env
$ source env/bin/activate
$ env> pip3 install -r requirements.txt
```

Run unit tests
```
$ env> python3 -m pytest -v
```

Get unit test coverage report
```
$ env> python3 -m pytest -v --cov
```

### Deployment

Define `$ROOT_DIR` 

Run
```
$ ./deploy.sh
```

### Using the Production App

Installation
```
$ cd $ROOT_DIR
$ python3 -m venv env
$ source env/bin/activate
$ env> pip3 install -r requirements.txt
```

Start App

Run the `main.py` file via your python interpreter
```
$ env> python3 main.py
```

Load user input

1. create/copy files that contain activities (following the user input file format) to `user_input` directory
2. use menu item 1 and specify the user input file name

Using the app

- Try out the menu points and see what peaks your interests