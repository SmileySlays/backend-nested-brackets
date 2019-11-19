#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Takes file and returns whether each line has valid brackets
"""
__author__ = "SmileySlays"

import sys


def main(args):
    input_list = []
    answer_list = []

    type_dict = {}
    type_list = ["parens", "curlies", "tags", "square", "weird_thing"]

    with open('input.txt', 'r') as f:
        for line in f:
            line += '_'
            temp = ''
            index = 0
            while index < len(line)-1:
                if line[index] == '(' and line[index+1] == '*':
                    temp += 'o'
                    index += 2
                elif line[index] == '*' and line[index+1] == ')':
                    temp += 'c'
                    index += 2
                else:
                    temp += line[index]
                    index += 1
            input_list.append(temp)

    for input_list_element in input_list:

        found = False
        for style in type_list:
            type_dict["{0}_stack".format(style)] = []
        for index, c in enumerate(input_list_element):

            if c == "o":
                type_dict["weird_thing_stack"].append(c)

            elif c == "c":

                try:
                    type_dict["weird_thing_stack"].pop()

                except Exception:
                    answer_list.append(("NO", index+1))
                    found = True
                    break

            if c == "(":
                type_dict["parens_stack"].append(c)

            elif c == ")":
                try:
                    type_dict["parens_stack"].pop()

                except Exception:
                    answer_list.append(("NO", index+1))
                    found = True
                    break

            if c == "{":
                type_dict["curlies_stack"].append(c)

            elif c == "}":

                try:
                    type_dict["curlies_stack"].pop()

                except Exception:
                    answer_list.append(("NO", index+1))
                    found = True
                    break

            if c == "[":
                type_dict["square_stack"].append(c)

            elif c == "]":

                try:
                    type_dict["square_stack"].pop()

                except Exception:
                    answer_list.append(("NO", index+1))
                    found = True
                    break

            if c == "<":
                type_dict["tags_stack"].append(c)

            elif c == ">":

                try:
                    type_dict["tags_stack"].pop()

                except Exception:
                    answer_list.append(("NO", index+1))
                    found = True
                    break

        if found:
            continue

        if len(type_dict["parens_stack"]) == 0 and len(type_dict["curlies_stack"]) == 0 and len(type_dict["square_stack"]) == 0 and len(type_dict["tags_stack"]) == 0:
            answer_list.append(("YES"))
        else:
            answer_list.append(("NO", index+1))

    return answer_list


# returned_list.append("NO" + str(index))
if __name__ == '__main__':
    with open("output.txt", "w+") as f:
        answer_list = main(sys.argv)
        for index, element in enumerate(answer_list):
            if len(element) == 2:
                f.write(str(answer_list[index][0]) + " " +
                        str(answer_list[index][1]) + "\n")
            else:
                f.write(str(answer_list[index]) + "\n")
