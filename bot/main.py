import sys

contacts = dict()


def parse_input(command):
    cmd = command.split()
    if not cmd and 0 == len(cmd):
        return None, None

    match cmd[0].lower():
        case 'exit' | 'close':
            return 'exit'
        case 'add':
            if len(cmd) == 3:
                return 'add', cmd[1:]
            else:
                print(f'Incorrect command: {command}')
                return None, None
        case 'change':
            if len(cmd) == 3:
                return 'change', cmd[1:]
            else:
                print(f'Incorrect command: {command}')
                return None, None
        case 'find':
            if len(cmd) == 2:
                return 'find', cmd[1:]
            else:
                print(f'Incorrect command: {command}')
                return None, None
        case 'list':
            return 'list', None
        case 'help':
            return 'help', None
        case _:
            return None, None


def add_handler(name, phone):
    contacts[name.lower()] = {'name': name, 'phone': phone}


def list_handler():
    for v in contacts.values():
        print(f'{v['name']}: {v['phone']}')


def find_handler(find):
    found = contacts.get(find.lower())
    if not found:
        print(f'{find} not found')
    else:
        print(f'{found["name"]}: {found["phone"]}')


def change_handler(name, phone):
    if contacts.get(name.lower()):
        contacts[name.lower()]['phone'] = phone
    else:
        contacts[name.lower()] = {'name': name, 'phone': phone}

    find_handler(name)

def print_help():
    print("""
    
        - add <name> <phone>
        - change <name> <phone>
        - find <name>
        - list - 
        - exit, close - for exit from program
        """)

def main():
    print("Hello in the ghost contact list. To operate please follow commands below")
    print_help()

    while True:
        command = input("Please enter your command: ")

        parsed_command, params = parse_input(command)

        match parsed_command:
            case None:
                print(f'{command} is not a valid command')
                print_help()
            case 'help':
                print_help()
            case 'exit':
                sys.exit(0)
            case 'add':
                add_handler(*params)
            case 'list':
                list_handler()
            case 'find':
                find_handler(params[0])
            case 'change':
                change_handler(*params)
            case _:
                print(f'Unknown command: {command}')
                print_help()


if __name__ == '__main__':
    main()
