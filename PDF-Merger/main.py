from PyPDF2 import PdfWriter
# Not Works for scanned pdf's
merger = PdfWriter()

pdfs = []

n = int(input("Enter the number of pdf's You want to merge : "))

for i in range(0, n):
    name = input(f"Enter the name of pdf {i+1} : ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)   # 

print("Merging PDF's.......")

merger.write("merged-pdf.pdf")
merger.close()

print("Done! PDFs merged successfully.")