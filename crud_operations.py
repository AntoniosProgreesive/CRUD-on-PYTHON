# crud_operations.py
# Ελληνικά: Αυτό το αρχείο περιέχει τις λειτουργίες για την διαχείριση των εγγραφών.
# English: This file contains the functions for managing records.

RECORDS_FILE = "records.txt"

def load_records():
    """
    Ελληνικά: Φορτώνει τις εγγραφές από το αρχείο.
    English: Loads the records from the file.
    """
    try:
        with open(RECORDS_FILE, "r") as file:
            records = [line.strip() for line in file.readlines()]
        return records
    except FileNotFoundError:
        return []

def save_records(records):
    """
    Ελληνικά: Σώζει τις εγγραφές στο αρχείο.
    English: Saves the records to the file.
    """
    with open(RECORDS_FILE, "w") as file:
        for record in records:
            file.write(record + "\n")

def add_record():
    """
    Ελληνικά: Προσθέτει μια νέα εγγραφή.
    English: Adds a new record.
    """
    new_record = input("Εισάγετε νέα εγγραφή / Enter new record: ")
    records = load_records()
    records.append(new_record)
    save_records(records)
    print("Η εγγραφή προστέθηκε επιτυχώς / Record added successfully.")

def edit_record():
    """
    Ελληνικά: Επεξεργάζεται μια υπάρχουσα εγγραφή.
    English: Edits an existing record.
    """
    records = load_records()
    for idx, record in enumerate(records):
        print(f"{idx + 1}. {record}")
    
    record_idx = int(input("Επιλέξτε αριθμό εγγραφής για επεξεργασία / Select record number to edit: ")) - 1
    if 0 <= record_idx < len(records):
        new_value = input("Εισάγετε νέα τιμή / Enter new value: ")
        records[record_idx] = new_value
        save_records(records)
        print("Η εγγραφή ενημερώθηκε επιτυχώς / Record updated successfully.")
    else:
        print("Μη έγκυρη επιλογή / Invalid selection.")

def delete_record():
    """
    Ελληνικά: Διαγράφει μια εγγραφή.
    English: Deletes a record.
    """
    records = load_records()
    for idx, record in enumerate(records):
        print(f"{idx + 1}. {record}")
    
    record_idx = int(input("Επιλέξτε αριθμό εγγραφής για διαγραφή / Select record number to delete: ")) - 1
    if 0 <= record_idx < len(records):
        records.pop(record_idx)
        save_records(records)
        print("Η εγγραφή διαγράφηκε επιτυχώς / Record deleted successfully.")
    else:
        print("Μη έγκυρη επιλογή / Invalid selection.")

def search_record():
    """
    Ελληνικά: Αναζητά μια εγγραφή με βάση το κείμενο.
    English: Searches for a record based on text.
    """
    query = input("Εισάγετε το κείμενο αναζήτησης / Enter search text: ")
    records = load_records()
    found = [record for record in records if query in record]
    if found:
        print("Βρέθηκαν τα εξής αποτελέσματα / The following results were found:")
        for record in found:
            print(record)
    else:
        print("Δεν βρέθηκαν αποτελέσματα / No results found.")

def list_records():
    """
    Ελληνικά: Εμφανίζει όλες τις εγγραφές.
    English: Displays all the records.
    """
    records = load_records()
    if records:
        print("Οι εγγραφές είναι / The records are:")
        for record in records:
            print(record)
    else:
        print("Δεν υπάρχουν εγγραφές / No records found.")
