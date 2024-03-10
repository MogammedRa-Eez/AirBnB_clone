#!/usr/bin/python3
"""
Define HBnB console.
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """ Defines the HolbertonBnB command interpreter """
    
    prompt = "(hbnb) "
    
    def do_EOF(self, arg): 
        """ Handles EOF to exit program """ 
        print() 
        return True

    def do_quit(self, args): 
        """ Quits the interpreter """  
        raise SystemExit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
