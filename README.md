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

Module - A .py file that has reusable functions or classes. NOT intended as a standalone script.

Package - A folder containg `__init__.py` that holds related modules. `numpy` for example.

NOTE: When importing you import a function or a class at a time. Or use * to grab all functions/classes.