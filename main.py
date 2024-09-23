# main.py
# Ελληνικά: Αυτό είναι το κύριο αρχείο που εκτελεί το πρόγραμμα.
# English: This is the main file that runs the program.

import menu
import crud_operations

def main():
    """
    Ελληνικά: Η κύρια συνάρτηση που ελέγχει τη ροή του προγράμματος.
    English: The main function that controls the flow of the program.
    1. Προσθήκη εγγραφής / Add record
    2. Επεξεργασία εγγραφής / Edit record
    3. Διαγραφή εγγραφής / Delete record
    4. Αναζήτηση εγγραφής / Search record
    5. Λίστα εγγραφών / List records
    6. Έξοδος / Exit
    """
    while True:
        menu.show_menu()
        choice = menu.get_user_choice()
        
        if choice == "1":
            crud_operations.add_record()
        elif choice == "2":
            crud_operations.edit_record()
        elif choice == "3":
            crud_operations.delete_record()
        elif choice == "4":
            crud_operations.search_record()
        elif choice == "5":
            crud_operations.list_records()
        elif choice == "6":
            print("Έξοδος από το πρόγραμμα / Exiting the program.")
            break
        else:
            print("Μη έγκυρη επιλογή / Invalid choice.")

if __name__ == "__main__":
    main()
