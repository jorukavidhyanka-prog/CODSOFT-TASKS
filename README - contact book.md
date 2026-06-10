# Contact Book Application

A simple command-line Contact Book built with Python. It allows users to add, view, search, and delete contacts while storing data in a JSON file.

## Features

- Add new contacts
- View all saved contacts
- Search contacts by name
- Delete contacts
- Persistent storage using JSON
- Easy-to-use command-line interface

## Requirements

- Python 3.7 or higher

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/contact-book.git
```

2. Navigate to the project directory:

```bash
cd contact-book
```

3. Run the application:

```bash
python contact_book.py
```

## Usage

### Main Menu

```text
===== Contact Book =====
1. Add Contact
2. View Contacts
3. Search Contact
4. Delete Contact
5. Exit
```

### Add Contact

Enter:
- Name
- Phone Number
- Email Address

### View Contacts

Displays all saved contacts.

### Search Contact

Search for a contact using a name or partial name.

### Delete Contact

Remove a contact by entering the exact name.

## Project Structure

```text
contact-book/
│
├── contact_book.py
├── contacts.json
└── README.md
```

## Example Contact Record

```json
{
    "name": "John Doe",
    "phone": "9876543210",
    "email": "john@example.com"
}
```

## Future Enhancements

- Update/Edit contacts
- Export contacts to CSV
- GUI version using Tkinter
- Contact grouping and favorites
- Password protection

## License

This project is licensed under the MIT License.

## Author

Your Name