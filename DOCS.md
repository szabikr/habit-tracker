# Habit Tracker Documentation

### Code Modules

- `main.py` is the main entry point of the application. It contains the **menu points** and it serve as the orchastrator of all high level features
- `import_activities.py`, `when_did_i_do.py` are considerred high level features which help the user to import their data and retrieve valuable information
  - `import_activities.py` imports activities defined in the `user_input` directory as user input files
  - `when_did_i_do.py` is a data extraction module that returns all the occurences of a specifi activity. Activity needs to be requested via the `activity_name`
- `activities` is a low level package that deals with the operation of the database and user input files, contains IO operations
- `tests` contains unit tests for the low level `activities` package

### Data Modules

- `user_input` is a directory that contains the user input files
- `data.txt` is the file based database
- `logs.txt` home for all the logs indicating the events that happened in the system

### User Input Files

Must be in the `user_input` directory.

Contents example

```
10 Aug
developing my habit tracker; Career
walk; Health & Fitness
talk to a friend; Friendship

11 Aug
cooking; Household
talk to a family member; Family
```

Format

```
{day of month} {month name, short version}
activity name 1; life aspect
activity name 2; life aspect
...
activity name n; life aspect

{day of month} {month name, short version}
...
```

### Database - data.txt

It's essentially a flat database containing activity definitions line by line

Contents example

```
d5ed9fe1-1ed9-4c93-864c-e71467873392; 2022-08-10; developing my habit tracker; Career
acc88000-e1f8-49fe-b8c2-78d3670f29b3; 2022-08-10; walk; Health & Fitness
c10e0aff-e45f-4554-9e71-7135cb890fdb; 2022-08-10; talking to a friend; Friendship
f3476995-7dee-4786-927c-2cfe6200b847; 2022-08-11; talking to a family member; Family
c76e7a40-1ac8-4c74-9fd2-00d31dfb1580; 2022-08-11; cooking; Household
```

Format

```
uuid; date(YYYY-MM-DD); activity_name; life_aspect
...
```

### Logging and Monitoring

Using the logging package from the python standard library and its configuration is defined in `log_config.yaml`. There are two logging handlers one for the console and the other for the filesystem.

`logs.txt` contains the saved logs and can be used to reconstruct events that happened in the system.

Contents example

```
2022-08-30 16:06:19,607 INFO: Begin importing activities from user input (habits_w1_10_14_aug.txt) to db...
2022-08-30 16:06:19,608 INFO: Reading user input activities from habits_w1_10_14_aug.txt
2022-08-30 16:06:19,613 INFO: Read 10 activity from user input file habits_w1_10_14_aug.txt
2022-08-30 16:06:19,613 INFO: Reading db activities from data.txt
2022-08-30 16:06:19,613 INFO: Read 0 activity from db file data.txt
2022-08-30 16:06:19,613 INFO: Opening data.txt for writing the activities
2022-08-30 16:06:19,614 INFO: Wrote 10 activities to data.txt
2022-08-30 16:06:19,614 INFO: Finished importing activities from user input to db file.
```

Format

```
{date} {time} {severity}: {message}
...
```
