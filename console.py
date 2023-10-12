import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
"""
This module creates a command interpreter providing a CLI
"""

class HBNBCommand(cmd.Cmd):
    """
    This class defines a command interpreter
    """
    prompt = "(hbnb) "
    __module_names = ["BaseModel", "User"]

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
        """Create a new instance"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.__module_names:
            print("** class doesn't exist **")
        else:
            new_class = BaseModel()
            new_class.save()
            print(new_class.id)

    def do_show(self, arg):
        """Display attributes of an instance"""
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
        """Delete an instance"""
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
        """Display all the instances with the attributes"""
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
        """Add a new attribute to an existing instance"""
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
