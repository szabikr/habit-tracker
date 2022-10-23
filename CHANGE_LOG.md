# v1.0.0 - Activities and Journal Entries

### Motivation

Want to introduce a journaling habit through this project and considered to write my daily journal entires in a separate file called `journal.txt` and parse that similarly to a `user_input` file.
However, I think it might just get a little too messy with multiple `user_input` files, so the solution is the bake the daily journal entries into the already existing `user_input` file format.

This is starting to get closer to the idea of habit journal. Whereby I have my habits, and a journal for each day so that I can introduce a more personal way of recording my activities. Would be nice to see my journal entries in the context of my habits, and see if there's any correlation between the two.

And to be honest the wrapped text file here in Vim doesn't seem that bad. Plus I don't want to do any correction to these journal entries really, can be just a brain dump or important stuff. I really just wanna get into the habit of journaling, that's all.

### Theoretical Solution

Currently we have the data.txt that contains all the data that is entered into the Habits database. And that `data.txt` file contains only the activities. Now that I'm doing journaling in the same application, I need a file called

- `activity.txt` contains the activities just as how it is the `data.txt`
- `journal.txt` contains the journal entries, with an UUID, journal_date, journal_entry

With this we are creating a dependency to the `user_input` files and their parsing. But thinking about it, that doesn't stop me putting together a CLI that allows adding journal entries from the command line directly. Also, I could just add different activities from that newly created CLI if I agree that the source of truth is the database, or perhaps the database files: `activity.txt` and `journal.txt`

Mixing the 2 concepts (`activity` and `journal_entry`) into a single user input file is a good first solution, but later on I can create another file that supports Markdown and maybe it has a journal entry for only one day, or for the entire week. I'll see, but for now the best solution is to couple the 2 concepts into the same `user_input` file, and have the python script separate them nicely.
