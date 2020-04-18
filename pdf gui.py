from tkinter import *
import tkinter
from tkinter import filedialog, messagebox
import PyPDF2

filename = ""
key = ""


window = tkinter.Tk(screenName=None, baseName=None, className='PDF', useTk=1)
window.geometry("500x400")
window.configure(background='turquoise')


def open_file():
    global filename
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("pdf file", "*.pdf"), ("all files", "*.*")))
    path.insert(0, filename)


openfilebutton = Button(window, command=open_file, text='Open File').place(x=300, y=100)
path = Entry(window)
path.place(x=100, y=100)


keyword = Entry(window)
keyword.place(x=100, y=200)



def extract():
    if filename is "":
        tkinter.messagebox.showinfo('Please select file','Please select file')

        return None

    key = keyword.get()
    if key == "" :
        tkinter.messagebox.showinfo('Enter word to search','Enter word to search')
        return None
    try:
        pdfFileObject = open(filename, 'rb')
    except:
        tkinter.messagebox.showinfo('File cant open','File cant open')
        return None

    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
    pdfWritter = PyPDF2.PdfFileWriter()
    count = 0
    output = 'pagenotest.txt'
    file = open(output, 'w')

    for i in range(pdfReader.numPages):
        pageObject = pdfReader.getPage(i)
        text = pageObject.extractText()
        if key in text or key.capitalize() in text or key.upper() in text or key.lower() in text:
            count = count + 1

            file.write(str(i + 1) + '\n')
            pdfWritter.addPage(pageObject)


    oytputpdf = 'outputpdf.pdf'
    pdfOutputFile = open(oytputpdf, 'wb')
    pdfWritter.write(pdfOutputFile)
    pdfOutputFile.close()
    file.close()
    pdfFileObject.close()


convert = Button(window, command=extract, text='Get File').place(x=200, y=300)

window.mainloop()
