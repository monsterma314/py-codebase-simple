## Python Codebase Simple Integration Example

- [x] Set up the `venv` using `python3 -m venv venv`
- [x] Set up to following directory structure:

``` bash
├── myMath
│   ├── __init__.py
│   ├── matematicas.py
├── README.md
├── src
│   ├── main
│   │   └── main.py
│   └── myPrints
│       ├── __init__.py
│       ├── printing_ints.py
└── venv
    ├── lib
    │   └── python3.6
    │       └── site-packages
    │           └── my-project-paths.pth
```

- [x] Create the code in `main.py` to use the packages `myPrints` and `myMath`


### Terms

Function - A python function exists in a .py file

Module - A .py file that has reusable functions or classes. NOT intended as a standalone script.

Package - A folder containg a `__init__.py` (can be blank decorator) to indicate a package

NOTE: When importing you import a function or a class at a time. Or use * to grab all functions/classes.