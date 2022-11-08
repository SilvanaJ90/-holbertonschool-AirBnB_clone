#!/usr/bin/python3
"""
console that contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
import models
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """ clas HBNB cmd """
    prompt = '(hbnb) '
    list_class = {
        "BaseModel": BaseModel,
        "User": User,
        "City": City,
        "State": State,
        "Review": Review,
        "Amenity": Amenity,
        "Place": Place
    }

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves JSON file"""
        command = self.parseline(arg)[0]
        if command is None:
            print("** class name missing **")
        elif command not in self.list_class:
            print("** class doesn't exist **")
        else:
            new_obj = eval(command)()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        command = self.parseline(arg)[0]
        arg = self.parseline(arg)[1]
        if command is None:
            print("** class name missing **")
        elif command not in self.list_class:
            print("** class doesn't exist **")
        elif arg == "":
            print("** instance id missing **")
        else:
            instance = models.storage.all().get(command + "." + arg)
            if instance is None:
                print("** no instance found **")
            else:
                print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        command = self.parseline(arg)[0]
        arg = self.parseline(arg)[1]
        if command is None:
            print("** class name missing **")
        elif command not in self.list_class:
            print("** class doesn't exist **")
        elif arg == "":
            print("** instance id missing **")
        else:
            key = command + "." + arg
            instance = models.storage.all().get(key)
            if instance is None:
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, arg):
        """Prints all string all instances based or not on the class name"""
        command = self.parseline(arg)[0]
        objs = models.storage.all()
        if command is None:
            print([str(objs[obj]) for obj in objs])
        elif command in self.list_class:
            keys = objs.keys()
            print([str(objs[key]) for key in keys if key.startswith(command)])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        listArg = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif self.parseline(arg)[0] not in self.list_class:
            print("** class doesn't exist **")
        elif len(listArg) == 1:
            print("** instance id missing **")
        elif len(listArg) == 2:
            print("** attribute name missing **")
        elif len(listArg) == 3:
            print("** value missing **")
        else:
            objs = models.storage.all()
            string = f'{listArg[0]}.{listArg[1]}'
            if string not in objs.keys():
                print("** no instance found **")
            else:
                setattr(objs[string], listArg[2], listArg[3])
                models.storage.save()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """ empty line """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
