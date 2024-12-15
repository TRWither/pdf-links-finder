import PyPDF2
import os
import requests

def getpath() -> int:
    pdfpath = input("Enter the path of the PDF file: ")
    if os.path.exists(pdfpath):
        return pdfpath
    elif os.path.isdir(pdfpath):
        print(f"{pdfpath} is a directory")
        return None
    else:
        print(f"{pdfpath} not found")
        return None

def is_url_valid(url: str) -> bool:
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.status_code >= 200 and response.status_code < 400
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return False

def findlinks(pdfpath: str) -> None:
    try:
        reader = PyPDF2.PdfReader(pdfpath)
        for page_num, page in enumerate(reader.pages, start=1):
            if "/Annots" in page:
                for annot in page["/Annots"]:
                    annot_object = annot.get_object()
                    if annot_object.get("/A") and annot_object["/A"].get("/URI"):
                        url = annot_object["/A"]["/URI"]
                        is_valid = is_url_valid(url)
                        print(f"Page {page_num}: {url} - {'Valid' if is_valid else 'Invalid'}")
    except Exception as e:
        print(f"An error occurred while processing the PDF: {e}")
