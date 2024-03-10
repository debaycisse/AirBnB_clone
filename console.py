#!/usr/bin/env python3
"""This module houses the HBNB class definition
and its attributes and methods"""

import cmd


class HBNBCommand(cmd.Cmd):
    """This class houses the configuration of the line-oriented
    interpreter interface for the AirBNB project"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """This is a quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """This method closes or terminates this session"""
        print()
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
