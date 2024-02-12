#!/usr/bin/python3
"""
Module for the command interpreter.
"""
import cmd
import models
from models.base_model import BaseModel
from models.__init__ import storage
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.city import City


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand is a class that inherits
    from cmd.Cmd for a basic command interpreter.
    """

    clasNames = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review,
    }
    prompt = "(hbnb) "

    def do_create(self, line):
        """Create new instances of BaseModel class"""

        if line:
            line = line.split(" ")
            if line[0] in self.clasNames:
                class_name = line[0]
                instance = self.clasNames[class_name]()
                instance.save()
                print(f"{instance.id}")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """A method that shows an instance of a
        class based on class name and id
        """

        check = self.validate(line)
        if check:
            line = line.split(" ")
            store = storage.all()
            key = f"{line[0]}.{line[1]}"

            if key in store:
                instance_dict = store[key]
                print(instance_dict)
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """A method that deletes an instance based on class name and id"""

        check = self.validate(line)
        if check:
            line = line.split(" ")
            store = models.storage.all()
            key = f"{line[0]}.{line[1]}"
            if key in store:
                class_name = line[0]
                instance_dict = store[key]
                instance_dict.delete()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Print all string representations of instances based
        on class name or all instances if no class name provided."""

        line = line.split()
        store = storage.all()

        if not line:
            # If no class name provided, print all instances
            instance = [str(insta) for insta in store.values()]
        elif line[0] in self.clasNames:
            # If class name provided, print instances of that class
            instance = [
                str(insta)
                for insta in store.values()
                if f"{line[0]}.{insta.id}" in store
            ]
        else:
            print("** class doesn't exist **")
            return

        print(instance)

    def do_update(self, line):
        """A method that updates the instance and saves it to a file"""
        check = self.validate(line)
        if check:
            line = line.split(" ")
            key = f"{line[0]}.{line[1]}"
            store = storage.all()
            if key in store:
                if len(line) >= 3:
                    if len(line) >= 4:
                        # Value validation
                        dict = store[key]
                        if len(line[3].split('"')) > 2:
                            val = line[3].split('"')[1]

                        elif "." in line[3]:
                            val = float(line[3])
                        else:
                            val = int(line[3])
                        # Update the existing instance
                        instance = store[key]
                        setattr(instance, line[2], val)
                        instance.save()
                    else:
                        print("** value missing **")
                else:
                    print("** attribute name missing **")
            else:
                print("** no instance found **")

    def do_count(self, line):
        """A model that  retrieve the number of instances of a class"""
        if line:
            if line in self.clasNames:
                store = storage.all()
                value = [i for i in store.values()]
                count = 0
                for i in value:
                    if type(i).__name__ == line:
                        count += 1
                print(count)
            else:
                print("** class doesn't exist **")

        else:
            print("** class name missing **")

    def do_quit(self, line):
        """
        A command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """
        Handles EOF to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on empty line.
        """
        pass

    def precmd(self, line):
        if line:
            if "." in line and "," not in line:
                line = line.replace(".", " ").replace("(", "").replace(")", "")
                lin = line.split(" ")
                try:
                    line = " ".join(reversed(lin))
                    lin = line.split('"')
                    line = lin[0] + lin[2] + " " + lin[1]
                except Exception:
                    pass

            elif "." in line and "," in line:
                line = line.replace(".", " ").replace("(", "").replace(")", "")
                lin = line.split(" ")
                lin = " ".join(lin)
                keep = lin
                keep = keep.split(",")
                first = keep[1].split('"')
                att = keep[0].split(" ")
                see = att[1].split('"')
                last = keep[1].split(" ")
                line = (
                    see[0]
                    + " "
                    + att[0]
                    + " "
                    + see[1].replace('"', "")
                    + " "
                    + first[0].strip()
                    + last[-1].replace('"', "")
                    + keep[-1]
                )

        return cmd.Cmd.precmd(self, line)

    def validate(self, line):
        """A method that validate requirement of inputs"""

        if line:
            line = line.split(" ")
            if line[0] in self.clasNames:
                if len(line) >= 2:
                    return True
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
