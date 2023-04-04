# PDF Merge script for bill printing

This file takes an input directory and then asks for an output file.  
It then merges all pdf files in the directory into one file for easy printing.
It has an if/else statement to check the number of pages in the input file and
adds a blank page at the end of each input file if the pages are odd.
This keeps the bills printing correctly so that the first page of one bill does not
print on the back of the previous bill.