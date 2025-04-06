# PDF Splitter
Script to (bulk) split PDF's into two PDF's, one with odd pages only, the other with even pages only. This is useful for double sided printing. 

## How to use?
- Download the script
- Install dependancies:
```
pip install PyPDF2
pip install pycryptodome
```
- Run script:
```
python split.py file1.pdf file2.pdf file3.pdf
```

This will produce a subfolder (or subfolders) by the same name as the original pdf file, and in the same directory. Inside the folders will be two new pdf's: `file1_even.pdf` and `file1_odd.pdf`. Use them how you wish. 

## split2.py
If you use this script, the order of the odd pages will be reversed, for ease of printing. This means that the odd pages will print, and you can immediately reinsert the pages for even pages. The even pages will however be in the wrong order, but you can't do much about that. ¯\_(ツ)_/¯
