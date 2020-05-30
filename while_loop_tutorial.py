command =""
started = False
while True:
    command = input("> ").lower()
    if command == 'start':
        if started:
            print( "Car already running")
        else:
            started = True
            print(" Start engine...")
    elif command == "stop":
        if not started:
            print("Car already stopped")
        else:
            started = False
            print("Engine stopped...")
    elif command == "quit":
        break
    elif command == 'help':
        print("""
Start- Starts engine
Stop - Stops engine
quit - Stops program
""")
    else:
        print("I don't understand!")


