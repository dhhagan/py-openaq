# Contributing to the `py-openaq` Documentation

The documentation style used for this project is based on that used by the
`seaborn` project and is based on sphinx and auto-doc for automatgically
generating documentation.

If you are interested in editing or improving the documentation, please be sure to read the entirety of this page.

## Fixing Issues with the API Documentation

The API documentation is automatically generated using sphinx-autodoc by taking the docstrings as defined in the source code and converting them. To edit these, you must edit the docstring located in the appropriate file, making sure to follow the sphinx format.

## Fixing (or adding) Tutorials

The tutorials section is automatically generated from the jupyter notebooks found in `/docs/tutorial`. To edit an existing tutorial, fire up a jupyter kernel and navigate to the appropriate file. Once open, you can edit all you want as if it were a normal notebook (because it is). Once complete, you can follow the steps below to generate the new html files that correspond to the notebook.

If you would like to add a new tutorial, there are a couple of steps to get up and running.

  1. Create a new notebook

        Create a new notebook as you typically would (post an issue if you need help with jupyter), and copy the format from another tutorial notebook. You may have to view the first cell as "raw", as there is some funky formatting that is required to make everything work.

  2. Add the notebook to the make file

        Open up the `/docs/tutorial/Makefile` and add a new row like `tools/nb_to_doc.py <name-of-file-without-ending-here>`

## Building Local Documentation

Finally, once you've edited your files, you can generate a new copy of the documentation by doing the following:

    >>> cd /docs
    >>> make clean
    >>> make notebooks
    >>> make html

You will then have a nice new set of docs to look at!
