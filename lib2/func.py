#!/usr/bin/python
# -*- coding: utf-8 -*-

TEMP_FF = "VANESSA"
TEMP_LISTE = ["Nummer 1"]

def add_list(neuer_eintrag):
    TEMP_LISTE.append(neuer_eintrag)

def print_name():
    print("Wir befinden uns im File func in der lib 2")

def main():
    print("File func")
    print(TEMP_FF)
    print()

if __name__ == '__main__':
    main()