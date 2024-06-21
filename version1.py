#import libraries
from PyPDF2 import PdfReader, PdfWriter
import pyttsx3

#path to pdf
path = "write_your_path_to pdf"

#read the pdf
reader = PdfReader(path)

#start a PDF Writer
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

#add metadata
writer.add_metadata(
    {
        "/Author": "Sreena Raavi",
        "/Subject": "Maharshi Story in Short",
        "/Title": "Telugu Movie Story",
    }
)

#rewrite the PDF including metadata
with open("C:\\Users\\SREENA RAAVI\\Documents\\python\\PyPDF2\\story3.pdf", 'wb') as f:
    writer.write(f)

#read metadata
meta = reader.metadata
print(meta.title)
print("Title of PDF: " + meta.title)
print("The subject of PDF: " + meta.subject)
print("Author: " + meta.author)

#number of pages
no_of_pgs = len(reader.pages)
print("This PDF is of " + str(no_of_pgs) +  " pages")

#define area of interest in PDF
parts =[]
def visitor_body(text, cm,tm,fontDict, fontSize):
    #tm has 6 param - a b c d e f , abcd - scaling, rotating and skewing, ef - x cord, y cord
    y = tm[5]
    if y > 50 and y < 720:
        parts.append(text)

#extract the text in ROI
for i in range(no_of_pgs):
    page = reader.pages[i]
    page.extract_text(visitor_text=visitor_body)
    text_body = "".join(parts)

#initiate the text-speech translator
engine = pyttsx3.init()

#set voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#rate
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)

#introduction and conclusion
intro = "Hello! This is the version one of audiobook project."
conclusion = "Thank You! Bye Bye! See ya!"

#read out the extracted data from PDF
engine.say(intro)
engine.say(text_body)
engine.say(conclusion)
engine.runAndWait()
engine.stop()