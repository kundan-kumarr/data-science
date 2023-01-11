#!/usr/bin/env python
# coding: utf-8

# # Python Programming 
# 
# Python is high level programming language which supports object-oriented and
# functional programming. It is dynamically-typed and garbage-collected.
# 
# - Python is case sensitive.
# - Spacing is important(use of indentation).
# - [PEP8 Guidelines](https://www.python.org/dev/peps/pep-0008/).
# - Each line of code to **80** characters, though **99** is okay for certain use cases.  [IBM for this ruling](https://softwareengineering.stackexchange.com/questions/148677/why-is-80-characters-the-standard-limit-for-code-width)
# 
# ## An example cell
# 
# With MyST Markdown, you can define code cells with a directive like so:

# In[1]:


print(2 + 2)


# When your book is built, the contents of any `{code-cell}` blocks will be
# executed with your default Jupyter kernel, and their outputs will be displayed
# in-line with the rest of your content.
# 
# ```{seealso}
# Jupyter Book uses [Jupytext](https://jupytext.readthedocs.io/en/latest/) to convert text-based files to notebooks, and can support [many other text-based notebook files](https://jupyterbook.org/file-types/jupytext.html).
# ```
# 
# ## Create a notebook with MyST Markdown
# 
# MyST Markdown notebooks are defined by two things:
# 
# 1. YAML metadata that is needed to understand if / how it should convert text files to notebooks (including information about the kernel needed).
#    See the YAML at the top of this page for example.
# 2. The presence of `{code-cell}` directives, which will be executed with your book.
# 
# That's all that is needed to get started!
# 
# ## Quickly add YAML metadata for MyST Notebooks
# 
# If you have a markdown file and you'd like to quickly add YAML metadata to it, so that Jupyter Book will treat it as a MyST Markdown Notebook, run the following command:
# 
# ```
# jupyter-book myst init path/to/markdownfile.md
# ```
