import os
import sys

# STUDENT 5 ADDITION: User management and system information
import platform
import users

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def display_help():
    print("\nAvailable Commands:")
    print(" help                -Show available commands")
    print(" clear               -Clear the terminal screen")
    print(" exit                -Shut down MiniOS")
    
    #Under File Management
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    
    #Under Process Management
    print("")
    print("")
    print("")
    print("")
    
    #Under Memory Management
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

def exit_os():
    print("\nMiniOSMTB is shutting down... \nBye, I'll miss you")
    sys.exit(0)

# STUDENT 5 ADDITION: System information command
def show_systeminfo():
    print("\n========================================")
    print("           SYSTEM INFORMATION")
    print("========================================")
    print("OS Name: MiniOS MTB")
    print("Version: 1.0")
    print(f"Architecture: {platform.architecture()[0]}")
    print("CPU: Virtual CPU (simulated)")
    print("Memory: 1024 MB (simulated)")
    print(f"User: {users.get_current_user()}")
    print("========================================\n")
    
#Brain of our code, means your logic is supposed to be inserted under defmain() 
def main():
    clear_screen()
    print("========================================================================================================================")
    print("                                                       MINIOS MTB                                                                                            ")
    print("========================================================================================================================")
    print("\nWelcome to MiniOSMTB!\n")


# STUDENT 5 ADDITION: Require a successful login before using MiniOS
    if users.login() is None:
        return

    
    while True:
        try:
            user_input = input("MiniOSMTB>").strip()
            if not user_input:
                continue
            
            parts = user_input.split()
            command = parts[0].lower()
            args = parts[1:]
        
            if command == "exit":
                exit_os()
            elif command == "help":
                display_help()
            elif command == "clear":
                clear_screen()
            # STUDENT 5 ADDITION: User and system commands
            elif command == "whoami":
                users.whoami()
            elif command == "systeminfo":
                show_systeminfo()
        
        
        
        
        
            else:
                print(f"\nUnknown command: '{command}'.")
                print("Type 'help' to see the available commands\n")
        
        except KeyboardInterrupt:
            exit_os() 

         # STUDENT 5 ADDITION: Catch unexpected errors so the CLI can continue
        except Exception as error:
            print(f"\nError: The command could not be completed: {error}")  

if __name__ == "__main__":
    main()