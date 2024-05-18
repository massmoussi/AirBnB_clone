#!/usr/bin/python3

import cmd
prompt = '(hbnb)'


class HBNBCommand(cmd.Cmd):

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("EOF command to EOF the program")


if __name__ == '__main__':

    HBNBCommand().cmdloop()
