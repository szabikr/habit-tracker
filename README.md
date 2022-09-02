# My Habit Tracker

### Run App

```
$ python3 -m venv env
$ source env/bin/activate
$ env> pip3 install -r requirements.txt
$ env> python3 main.py
```

- Importing activities happens via the user input files defined in the `user_input` directory. This import will merge the already existing activities with the new ones
- When did I do feature gives back all the occurrences of an activity by specifying the `activity_name`

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

Define `$HBT_APP_ROOT_DIR` variable which is the directory where the Habit Tracker app should be deployed to.

Run
```
$ ./deploy.sh
```

### Using the Production App

Installation
```
$ cd $HBT_APP_ROOT_DIR
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