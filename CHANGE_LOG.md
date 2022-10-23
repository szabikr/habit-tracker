20 Oct
Maybe I should just start writing the journal in a completely new text file called `journal.txt` and potentially usea markdown
I might be a bit nicer to deal with, but at the same time I can end up in a situation where I use the `habits.txt` however not use the `journal.txt` so might be good idea to have it written and parsed in one go. Also I feel that it might be a good idea to keep the journal entries next to the habits, it would just mean that I completed the journaling habit.
And this is going to get close to the idea of habit journal. Whereby I have my habits, and a journal for each day so that I can introduce my feelings into this and also the evaluation of the days and so on. Would be nice to see all this in the context of my habits. And to be honest the wrapped text file here in Vim doesn't seem that bad. Plus I don't want to do any correction to these journal entries really, can be just a brain dump or important stuff. I really just wanna get into the habit of journaling, that's all.
Doing journaling in the same application is a good idea I think, cuz now I won't need to think about where to put my journal entries. It's not going to have a full on MarkDown feature like Notion has for example, but at least I'm going to own the data and I will be able to do with that data whatever the hell I want.

Currently we have the data.txt that contains all the data that is entered into the Habits database. And that `data.txt` file contains only the activities. Now that I'm doing journaling in the same application, I need a file called

- `activity.txt` contains the activities just as how it is the `data.txt`
- `journal.txt` contains the journal entries, with an UUID, journal_date, journal_entry

With this I'm creating a dependency to the user_input files and their parsing. But thinking about it, that doesn't stop me putting together a CLI that allows adding journal entries from the command line directly. Also, I could just add different activities from that newly created CLI if I agree that the source of truth is the database, or perhaps the database files: `activity.txt` and `journal.txt`

And mixing the 2 concepts (activity and journal entry) into a single user input file is a good first solution, but later on I can create another file that supports Markdown and maybe it has a journal entry for only one day, or for the netire week. I'll see, but for now the best solution is to couple the 2 concepts into the same user_input file, and have the python script separate them nicely.
