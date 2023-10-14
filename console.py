import cmd
import re
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

"""
This module creates a command interpreter providing a CLI
"""


class HBNBCommand(cmd.Cmd):
    """
    This class defines a command interpreter
    """
    class_count = {}
    prompt = "(hbnb) "
    __module_names = \
        ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """ Exits the program """
        return True

    def emptyline(self):
        """Handle the empty line case"""
        pass

    def do_create(self, arg):
        """
        Create a new instance
        
        Args:
            arg (str): Command passed into the interpreter
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.__module_names:
            print("** class doesn't exist **")
        else:
            args = arg.split()
            class_name = args[0]
            new_class = globals()[class_name]()
            new_class.save()
            print(new_class.id)

    def do_show(self, arg):
        """
        Display attributes of an instance
        
        Args:
            arg (str): Command passed into the interpreter
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__module_names:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            all_obj = storage.all()
            instance = all_obj.get(key, None)
            if instance:
                print(instance)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance
        
        Args:
            arg (str): Command passed into the interpreter
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__module_names:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Display all the instances with the attributes
        
        Args:
            arg (str): Command passed into the interpreter
        """
        args = arg.split()
        all_obj = storage.all()
        obj_list = []

        if not args:
            for obj in all_obj.values():
                obj_list.append(str(obj))
            print(obj_list)
        elif args[0] not in HBNBCommand.__module_names:
            print("** class doesn't exist **")
        else:
            for key, obj in all_obj.items():
                class_name, obj_id = key.split(".")
                if class_name == args[0]:
                    obj_list.append(str(obj))
                print(obj_list)

    def do_update(self, arg):
        """
        Add a new attribute to an existing instance
        
        Args:
            arg (str): Command passed into the interpreter
        """
        args = arg.split()

        all_obj = storage.all()

        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__module_names:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif not (storage.all().get(f"{args[0]}.{args[1]}", None)):
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            obj = all_obj[key]
            try:
                args[3] = eval(args[3])
            except (NameError, SyntaxError):
                pass
            setattr(obj, args[2], args[3])
            obj.save()

    def do_count(self, arg):
        """Count the number of instances of a class
        
        Args:
            arg (str): Command passed into the interpreter
        """
        objs = storage.all()
        obj_names = list(map(lambda obj: type(obj).__name__, objs.values()))
        print(f"{obj_names.count(arg)}")
        
    def precmd(self, arg):
        """
        Intercepts the command before it is invoked
        
        Args:
            arg (str): Command passed into the interpreter
        """
        if "." in arg and "(" in arg and ")" in arg:
            match = re.match(r"([A-Za-z_]\w*)\.([A-Za-z_]\w*)\((.*)\)", arg)
            if match:
                class_name, command, id = match.groups()
                id = id.strip('\'"')
                arg = f"{command} {class_name} {id}"
        return cmd.Cmd.precmd(self, arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
