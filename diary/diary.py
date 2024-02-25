from cryptography.fernet import Fernet
import os

class Diary:
    def __init__(self, key):
        self.key = key

    def encrypt_entry(self, entry):
        cipher_suite = Fernet(self.key)
        encrypted_entry = cipher_suite.encrypt(entry.encode())
        return encrypted_entry

    def decrypt_entry(self, encrypted_entry):
        cipher_suite = Fernet(self.key)
        decrypted_entry = cipher_suite.decrypt(encrypted_entry).decode()
        return decrypted_entry

    def write_entry(self, entry):
        with open('diary.txt', 'a') as f:
            encrypted_entry = self.encrypt_entry(entry)
            f.write(encrypted_entry.decode() + '\n')

    def read_entries(self):
        entries = []
        if os.path.exists('diary.txt'):
            with open('diary.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    decrypted_entry = self.decrypt_entry(line.encode())
                    entries.append(decrypted_entry)
        return entries

def main():
    key = Fernet.generate_key()
    diary = Diary(key)

    while True:
        print("\n1. Write an entry")
        print("2. View all entries")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            entry = input("Write your entry: ")
            diary.write_entry(entry)
            print("Entry saved successfully!")
        elif choice == '2':
            entries = diary.read_entries()
            print("\n--- Your Entries ---")
            for idx, entry in enumerate(entries, 1):
                print(f"{idx}. {entry}")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()