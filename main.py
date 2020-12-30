#!/usr/bin/python
# -*- coding: utf-8 -*-
# https://www.programiz.com/python-programming/package
import lib.func3
from lib import func, func2
from lib.func3 import get_num

# Test ohne __init__.py im lib Verzeichnis
def main():
    print("test 1")
    func.print_name()
    func2.print_name()
    lib.func3.print_name()
    print(get_num())

if __name__ == '__main__':
    main()