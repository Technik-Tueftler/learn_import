#!/usr/bin/python
# -*- coding: utf-8 -*-
import lib2
#2 from lib2.cmds import testfile
from lib2 import func3

def main():
    print("test 2")
    lib2.print_name()
    #2 testfile.print_name()
    # func.print_name()
    # func2.print_name()
    # lib.func3.print_name()
    func3.print_name()
    print(lib2.TEMP_VAR)
    print(lib2.TEMP_FF)
    print(lib2.TEMP_LISTE)
    lib2.add_list("TestString")
    print(lib2.TEMP_LISTE)
    lib2.print_lala()
    lib2.testlalaprint()

if __name__ == '__main__':
    main()
