if __name__ == '__main__':
    N = int(input()) # Pehle batao kitni commands aayengi
    my_list = []
    
    for _ in range(N):
        # Input ko split karo (Command aur uske numbers)
        command_input = input().split()
        cmd = command_input[0] # Pehla word command hai (e.g., 'insert')
        args = command_input[1:] # Baaki words numbers hain
        
        if cmd == "insert":
            my_list.insert(int(args[0]), int(args[1]))
        elif cmd == "print":
            print(my_list)
        elif cmd == "remove":
            my_list.remove(int(args[0]))
        elif cmd == "append":
            my_list.append(int(args[0]))
        elif cmd == "sort":
            my_list.sort()
        elif cmd == "pop":
            my_list.pop()
        elif cmd == "reverse":
            my_list.reverse()
