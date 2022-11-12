# My Habit Tracker

### Run App

```
$ python3 -m venv env
$ source env/bin/activate
$ env> pip3 install -r requirements.txt
$ env> python3 -m pip install -e .       # Install the local packages (-e for editable)
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
$ env> python3 -m pip install .     # Install the local packages
```

Start App

Run the `main.py` file via your python interpreter

```
$ env> python3 main.py {filename}
```

where `filename` is the name of the file in the `user_input` directory that you want to import.
