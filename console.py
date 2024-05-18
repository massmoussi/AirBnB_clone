#!/usr/bin/env python3

import cmd

class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def preloop(self):
        """Print a blank line before the command loop starts"""
        print()

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def help_EOF(self):
        print("EOF command to exit the program")

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def postloop(self):
        """Ensure a newline after command loop ends"""
        print()

    def precmd(self, line):
        """Print a blank line before each command"""
        print()
        return line


if __name__ == '__main__':
    HBNBCommand().cmdloop()
