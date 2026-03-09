class SimpleCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, text):
        encrypted_chars = []
        for i in range(len(text)):
            ch = text[i]
            key_ch = self.key[i % len(self.key)]
            encrypted_chars.append(chr(ord(ch) ^ ord(key_ch)))
        return ''.join(encrypted_chars)

    def decrypt(self, encrypted_text):
        return self.encrypt(encrypted_text)


class PasswordEntry:
    def __init__(self, website, username, encrypted_password):
        self.website = website
        self.username = username
        self.encrypted_password = encrypted_password

    def __str__(self):
        return f"Website: {self.website}, Username: {self.username}"


class PasswordManager:
    def __init__(self, master_key):
        self.cipher = SimpleCipher(master_key)
        self.passwords = {}

    def add_password(self, website, username, password):
        encrypted = self.cipher.encrypt(password)
        entry = PasswordEntry(website, username, encrypted)
        self.passwords[website] = entry
        print(f"Password saved for {website}")

    def edit_password(self, website, new_username=None, new_password=None):
        if website in self.passwords:
            entry = self.passwords[website]

            if new_username:
                entry.username = new_username

            if new_password:
                entry.encrypted_password = self.cipher.encrypt(new_password)

            print(f"Password details updated for {website}")
        else:
            print("Website not found")

    def retrieve_password(self, website):
        if website in self.passwords:
            entry = self.passwords[website]
            decrypted_password = self.cipher.decrypt(entry.encrypted_password)
            print(f"Website: {entry.website}")
            print(f"Username: {entry.username}")
            print(f"Password: {decrypted_password}")
        else:
            print("Website not found")

    def list_accounts(self):
        if not self.passwords:
            print("No passwords stored")
        else:
            print("\nStored Accounts:")
            for website, entry in self.passwords.items():
                print(entry)