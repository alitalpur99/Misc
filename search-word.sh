#!/bin/bash
#Search most common string in a text file

tr -c '[:alnum:]' '[\n*]' < test.txt | sort | uniq -c | sort -nr | head  -10
