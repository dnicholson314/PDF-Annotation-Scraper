import tkinter as tk
from tkinter import filedialog

import traceback as tb

from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, TextStringObject, IndirectObject
from pypdf.errors import PdfStreamError


greeting_message = """\
    Hello! This application will redact the author names from all annotations
    in a given pdf. Once you press ENTER, you will be presented with a file
    dialog to choose the PDF you would like to redact the author names from.
    Once the names are redacted, the application will return a success message.

    Press ENTER to continue.
"""

success_message = """
    Successfully redacted author names from annotations!

    Press ENTER to quit.
"""

COLORS = {
    "WARNING": '\033[93m',
    "ENDC": '\033[0m',
}

def str_with_color(string: str, color: str) -> str:
    end = COLORS["ENDC"]
    if color not in COLORS.values() or color == end:
        print(":)")
        return string

    return color + string + end

def handle_exception(e):
    print()
    print("Encountered exception ----------------------------------")
    tb.print_exception(e)
    print("--------------------------------------------------------")
    input("Press ENTER to continue.")

def redact_annotation_author(annot: IndirectObject):
    obj = annot.get_object()
    if "/T" not in obj:
        return

    obj.update(
        {
            NameObject("/T"): TextStringObject("")
        }
    )

def main():
    tk.Tk().withdraw()

    input(greeting_message)

    file_dir = filedialog.askopenfilename()

    try:
        reader = PdfReader(file_dir)
    except FileNotFoundError as e:
        raise FileNotFoundError(
           str_with_color("Did you close the file dialog without opening a file?",
                          COLORS["WARNING"])
        ) from e
    except PdfStreamError as e:
        raise PdfStreamError(
            str_with_color("Did you choose a file that was not a .pdf?",
                           COLORS["WARNING"])
        ) from e

    writer = PdfWriter()

    for page in reader.pages:
        if "/Annots" in page:
            for annot in page["/Annots"]:
                redact_annotation_author(annot)

        writer.add_page(page)

    with open(file_dir, "wb") as fp:
        writer.write(fp)

    input(success_message)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        handle_exception(e)