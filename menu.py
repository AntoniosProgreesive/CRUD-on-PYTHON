# menu.py
# Ελληνικά: Αυτό το αρχείο περιέχει το μενού που εμφανίζει τις επιλογές CRUD στον χρήστη.
# English: This file contains the menu that displays the CRUD options to the user.

def show_menu():
    """
    Ελληνικά: Εμφανίζει το μενού στον χρήστη.
    English: Displays the menu to the user.
    """
    print("1. Προσθήκη εγγραφής / Add record")
    print("2. Επεξεργασία εγγραφής / Edit record")
    print("3. Διαγραφή εγγραφής / Delete record")
    print("4. Αναζήτηση εγγραφής / Search record")
    print("5. Λίστα εγγραφών / List records")
    print("6. Έξοδος / Exit")

def get_user_choice():
    """
    Ελληνικά: Λαμβάνει την επιλογή του χρήστη από το μενού.
    English: Gets the user's choice from the menu.
    """
    choice = input("Επιλέξτε μια επιλογή / Choose an option: ")
    return choice
