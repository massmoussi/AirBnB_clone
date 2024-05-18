#!/usr/bin/env python3
"""
Console module for the HBNB command interpreter.
"""

import cmd
import sys


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


def run_interactive():
    """Run the command interpreter in interactive mode."""
    HBNBCommand().cmdloop()


def run_non_interactive():
    """Run the command interpreter in non-interactive mode."""
    for line in sys.stdin:
        cmd = line.strip()
        if cmd:
            print("(hbnb)")
            HBNBCommand().onecmd(cmd)


if __name__ == '__main__':
    if sys.stdin.isatty():
        run_interactive()
    else:
        run_non_interactive()
