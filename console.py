#!/usr/bin/env python3
"""
Console module for the HBNB command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "

    def emptyline(self):
        """Override emptyline method to do nothing."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF."""
        print()
        return True

    def help_quit(self):
        """Print help message for the quit command."""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Print help message for EOF."""
        print("Exit the program on EOF")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
