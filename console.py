#!/usr/bin/python3
"""
Define HBnB console.
"""


class HBNBCommand(cmd.Cmd):
    """
    Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """
    
    intro = 'Welcome to the interpreter! Type help or ? to list commands.\n'
    prompt = '(hbnb) '
    
    def do_EOF(self, arg): 
        """ Handles EOF to exit program """ 
        print() 
        return True

    def do_quit(self, args): 
        """ Quits the interpreter """  
        raise SystemExit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
