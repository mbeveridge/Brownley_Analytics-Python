# Foundations for Analytics with Python
#### From Non-Programmer to Hacker
###### Clinton W. Brownley

---

Publisher's [web page for this book](http://shop.oreilly.com/product/0636920038375.do), including [errata](https://www.oreilly.com/catalog/errata.csp?isbn=0636920038375)

Author's [blog post](https://cbrownley.wordpress.com/2016/03/02/foundations-for-analytics-with-python-from-non-programmer-to-hacker/) about the book

[Page xvii] All of the Python scripts, input files, and output files are available at [https://github.com/cbrownley/foundations-for-analytics-with-python](https://github.com/cbrownley/foundations-for-analytics-with-python)


| Directory or file (in root) | Explanation |
| --- | --- |
| ~d3/~ | ~[Chapter4] Latest version of d3.js, from [https://d3js.org](https://d3js.org). ("v5.9.2 Copyright 2019")~ |
| ~d3-book-2.0.3/~ | ~[Chapter1] Latest version (2.0.3) of sample files, from [GitHub releases page](https://github.com/alignedleft/d3-book/releases). (Includes d3.js "Version 4.5.0. Copyright 2017")~ |
| ~d3.js~ | ~[Chapter4] Library actually being used. Copy of a file in `d3/`. ("v5.9.2 Copyright 2019")~ |
| ~index.html~ | ~[Chapter4] Empty document~ |
| README.md | This document |

---

## 1. Python Basics *[P.1-58]*

* 'shebang' for Unix computers to find the version of Python to use (eg. `#!/usr/bin/env python3`) ...P.2
* `chmod +x first_script.py` (in Terminal) to make the Python script executable ...P.6
* `Ctrl+c` to stop a script ...P.7
* Regular expressions (`re` module) ...P.19
* good practice to `compile()` the regular expression (but not always necessary) ...P.20
* good practice to use raw string notation (`r`) in regular expressions ...P.20
* data types : numbers, strings, dates
* data containers : lists, tuples, dictionaries
* programming concepts : control flow, functions, exceptions


## 2. Comma-Separated Values (CSV) Files *[P.59-100]*

* `csv` module
* three types of conditional logic to filter for specific rows
* two ways to filter for specific columns
* multiple CSV files


## 3. Excel Files *[P.101-142]*

* `xlrd` module
* format dates so they appear as dates
* three types of conditional logic to filter for specific rows
* two ways to filter for specific columns
* multiple worksheets
* multiple workbooks


## 4. Databases *[P.143-177]*

* `sqlite3` module
* how to interact with MySQL


## 5. Applications *[P.179-213]*

* application1 : find specific records in a large collection of Excel & CSV files
* application2 : group or 'bin' data and calculate stats. [Creating a function; storing data in a dictionary; keeping track of previous & current rows]


## 6. Figures and Plots *[P.215-231]*

* plotting libraries : `matplotlib`, `pandas`, `ggplot`, `seaborn`


## 7. Descriptive Statistics and Modeling *[P.239-259]*

* `pandas` package
* `statsmodel` package
* multivariate linear regression and logistic classification models based on data in `pandas` DataFrames


## 8. Scheduling Scripts to Run Automatically *[P.261-273]*


## 9. Where to Go from Here *[P.277-295]*

* built-in modules : `collections`, `random`, `statistics`, `itertools`, `operator`
* built-in functions : `enumerate`, `filter`, `reduce`, `zip`
* add-in modules : NumPy, SciPy, Scikit-Learn
* additional data structures : stacks, queues, trees, graphs


## APPENDICES

