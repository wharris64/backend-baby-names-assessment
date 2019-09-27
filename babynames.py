#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
import os
import sys
import re
import argparse

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it done
 -Extract the names and rank numbers and just print them done
 -Get the names data into a dict and print it done
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    ranked_dict = {}
    ordered_names= []
    names_dict = {}
    with open(filename, 'r') as f:
        text = f.read()
    year_check = re.findall(r'Popularity\sin\s(\d\d\d\d)', text)
    year = year_check[0]
    name_check = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
    names = name_check
    
    #print(names[0])
    ordered_names.append(year)
    for name in names:
        rank, guy, girl = name
        if guy not in names_dict:
            names_dict[guy] = rank
        if girl not in names_dict:
            names_dict[girl] = rank
        new_world_order = sorted(names_dict)
    for hat in new_world_order:
        ordered_names.append("{} {}".format(hat, names_dict[hat]))
    text = '\n'.join(ordered_names) + '\n'
        
        
    #ordered_dict = sorted(names_dict)
    #new_world_order.insert(0, year)
    
    #for alpha_names in ordered_dict:
     #   if alpha_names == names_dict.key:
      #      temp_val=concat j and names_dict.value
       #     orderednames.append(temp_val)
    #cat = new_world_order[1]
 #return new_world_order
    #return names_dict
    #return ordered_dict
    #return year
    return text


def create_parser():
    """Create a cmd line parser object with 2 argument definitions"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more filenames.
    # It will also expand wildcards just like the shell, e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    #print(args)
    #print(args.files)
    

    if not args:
        parser.print_usage()
        sys.exit(1)
    create_summary = args.summaryfile
    
    file_list = args.files
    for filename in file_list:
        extracted_data = extract_names(filename)
        if create_summary:
            with open(filename + ".summary", "w") as f:
                f.write(extracted_data)
        else:
            print(extracted_data)
        


    # option flag
    


    # +++your code here+++
    
    # For each filename, get the names, then either print the text output
    # or write it to a summary file


if __name__ == '__main__':
        main()
