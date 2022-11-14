contacts={}

def input_error(func):
    def inner(data):
        try:
            result = func(data)
            return result
        except KeyError:
            print("User with such name is not available.")
        except ValueError:
            print("Name and phone are not given.")
        except IndexError:
            print("Name and phone are not given.")
    return inner

def hello(_):
    print('How can I help you?')

@input_error
def add(contact):
    name=contact[0]
    phone=contact[1]
    contacts[name]=phone
    print (f'Number {phone} with name {name} was added.')

@input_error
def change(contact):
    name=contact[0]
    phone=contact[1]
    for key in contacts.keys():
        if key == name:
            contacts[key] = phone
            print (f'Number {phone} with name {name} was changed.')
        else:
            print (f'Number {phone} with name {name} does not exist.')

@input_error
def phone(contact):
    print (f'{contact} number is {contacts[contact[0]]}.')     

def show_all(_):
    if len(contacts)>0:
        print('There are all contacts:')
        for name, phone in contacts.items():
            print(f'{name} : {phone}')
    else:
        print('There are no contacts.')

def bye(_):
    print('Good bye!')
    exit()

def unknown_action(_):
    print('Such command is not available')

COMMANDS = {
    'hello': hello,
    'add': add,
    'change': change,
    'phone': phone,
    'show all': show_all,
    'good bye': bye,
    'exit': bye,
    'close': bye
    }

def handler_input(input):
    input = input.lower().split(' ')
    command=input[0]
    if command in ('show', 'good'):
        command+=' '+input[1]
    info=input[1:]
    try:
        handler = COMMANDS[command]
    except KeyError:
        handler = unknown_action
        if not command or command == '.':
            handler = bye
    return handler, info


def main():
    print('Input one of this commands: hello, add (name phone), change (name phone), phone (phone), show all.')
    print('To stop the bot, input good bye, close, exit or .')
    while True:
        command=input('Input command: ')
        handler,info=handler_input(command)
        try:
            handler(info)
        except KeyError:
            print('Such command is not available')
main()