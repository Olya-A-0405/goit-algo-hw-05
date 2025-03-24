def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact does not exist."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner

contacts = {}

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError

@input_error
def get_phone(args, contacts):
    name = args[0]
    return contacts[name]

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def main():
    while True:
        command = input("Enter a command: ").strip().lower()
        if command == "add":
            args = input("Enter name and phone: ").split()
            print(add_contact(args, contacts))
        elif command == "change":
            args = input("Enter name and new phone: ").split()
            print(change_contact(args, contacts))
        elif command == "phone":
            args = input("Enter name: ").split()
            print(get_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command in ["exit", "close"]:
            print("Good bye!")
            break
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()
