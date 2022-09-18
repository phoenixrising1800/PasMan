import signal
from getpass import getpass

## Signal handler
def handler(signum, frame):
    exit(1)
signal.signal(signal.SIGINT, handler)

def main():
    # Step 0: Ask user to init new DB instance or choose existing instance
    print("Type CTRL-c at any time to quit")
    b = 0
    while (b != 'Y' or b != 'y' or b != 'N' or b != 'n'):
        b = input("Initialize new password database instance? (Y\\n): ")
        if (b == 'N' or b == 'n'):
            # call function
            print("This feature is not implemented yet") 
            exit(1)
        elif (b == 'Y' or b == 'y'):
            initdb()
            exit(1)
    
def initdb():
    # Step 1: Retrieve master password from user (op: key file path)
    p1, p2 = 0, 1
    while (p1 != p2):
        p1 = getpass("Enter your master password: ")
        p2 = getpass("Verify your master password: ")
        if (p1 != p2):
            print("\nPasswords don't match. Try again\n")
    P = p1 # user master password
    print(P)
    return

if __name__ == '__main__':
    main()
