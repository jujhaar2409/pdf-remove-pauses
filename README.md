# Remove pauses from beamer slides using python

Place your pdf files in the `pdfs` directory.

run `python3 remove_pauses.py`

The output will be stored in the directory `out`.

## ImportError on some older versions of python

If you face an import error which looks something like `ImportError: cannot import name 'PdfWriter' from 'PyPDF2'` then either use a newer version of python, if you have that on your system, or use the code on the branch `old-python` instead:

```bash
git checkout old-python
```
