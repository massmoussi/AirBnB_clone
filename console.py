#!/usr/bin/env python3

import cmd
from models.base_model import BaseModel
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in globals():
            print("** class doesn't exist **")
            return
        new_instance = globals()[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        instance = storage.all().get(key)
        if instance is None:
            print("** no instance found **")
            return
        print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        if arg and arg not in globals():
            print("** class doesn't exist **")
            return
        instances = storage.all()
        if arg:
            instances = {k: v for k, v in instances.items() if k.startswith(arg)}
        print([str(instance) for instance in instances.values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        instance = storage.all().get(key)
        if instance is None:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        setattr(instance, args[2], eval(args[3]))
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
