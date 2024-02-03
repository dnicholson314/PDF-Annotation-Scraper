# PDF Annotation Scraper

This application will redact the authors from any annotations in a PDF.
It is for use in applications where knowing the authors of annotations is
undesirable: for example, a double-blind journal where revisions are sent
directly to authors as PDFs.

I created this application for use at the Rawlings School of Divinity
journal [_Eleutheria_](https://digitalcommons.liberty.edu/eleu/). As a result,
it is tailored for personal use. However, pull requests are welcomed if any
issues arise with the application.

## Requirements

The application was built in Python 3.12 but should work for any Python
version since 3.8.

In terms of dependencies, `requirements.txt` contains all the necessary packages,
and the following instructions work through installing those packages for
use on your computer.

## Instructions

First, clone the repository to a local folder:

```bash
git clone https://github.com/dnicholson314/PDF-Annotation-Scraper.git
```

Then open a terminal and navigate to the working directory. Run the following
command to install the dependencies:

```bash
pip install -r requirements.txt
```

Finally, run the following command to launch the application:

```bash
python main.py
```
