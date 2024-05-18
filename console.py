#!/usr/bin/env python3

import cmd


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
