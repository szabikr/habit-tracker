import sys

from ht_importer.import_user_input import import_user_input

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Specify the user input file and try again.")
    
    filename = sys.argv[1]

    entity_counts = import_user_input(filename)

    print(f"Imported {entity_counts.activity_count} activities")
    print(f"Imported {entity_counts.journal_entry_count} journal entries")
