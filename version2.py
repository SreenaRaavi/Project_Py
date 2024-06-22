import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter
import pyttsx3

# Create a window
window = tk.Tk()
window.title("PDF to Audio Reader")

# Configure the window
window.rowconfigure([0,1,2,3], minsize=50, weight=1)
window.columnconfigure([0,1], minsize=50, weight=1)

#create a frame
frame = tk.Frame(master=window, height=3)
frame.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

#add a label
title = tk.Label(master=frame, text="PDF to Audio Reader")
title.pack()

#create another frame 
frame2 = tk.Frame(master=window)
frame2.pack(fill=tk.BOTH, expand=True)

# Browse the file 
def browse(): 
    # Get the file path
    file_path = filedialog.askopenfilename()

    # Rewrite the path
    path = file_path.split("/")
    file_path = "\\".join(path)
    
    # Read the name of the file
    name = path[-1]

    # Call the function to read the file in the given path
    read_pdf(file_path, name)

# Read the contents of file
def read_pdf(path, name):

    # Read the PDF of given path
    reader = PdfReader(path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    # Add metadata
    writer.add_metadata(
        {
            "/Author": "Sreena Raavi",
            "/Title": name,
        }
    )

    # Rewrite the PDF including metadata
    with open(path, 'wb') as f:
        writer.write(f)

    # Read metadata
    meta = reader.metadata
    print("Title of PDF: " + (meta.title if meta.title else "None"))
    print("Author: " + (meta.author if meta.author else "None"))

    # Number of pages
    no_of_pgs = len(reader.pages)
    print("This PDF is of " + str(no_of_pgs) +  " pages")

    #define area of interest in PDF
    parts =[]
    def visitor_body(text, cm,tm,fontDict, fontSize):
        y = tm[5]
        if y > 50 and y < 720:
            parts.append(text)

    #extract the text in ROI
    for i in range(no_of_pgs):
        page = reader.pages[i]
        page.extract_text(visitor_text=visitor_body)
        text_body = " ".join(parts)

    voice_over(text_body)

def voice_over(text):
    # Initiate the text-speech translator
    engine = pyttsx3.init()

    # Set voice
    f_or_m = voice_over_entry.get()
    voices = engine.getProperty('voices')
    if f_or_m.lower() == "female":
        audio = voices[1].id
    elif f_or_m.lower() == "male":
        audio = voices[0].id
    else:
        audio = voices[0].id  # Default to male if input is incorrect
    engine.setProperty('voice', audio)

    #set rate
    rate = int(num["text"])
    if rate > 50:
        engine.setProperty('rate', rate)
    else:
        engine.setProperty('rate', 175)

    # Introduction and conclusion
    intro = "Hello! This is the version one of audiobook project."
    conclusion = "Thank You! Bye Bye! See ya!"

    # Read out the extracted data from PDF
    engine.say(intro)
    engine.say(text)
    engine.say(conclusion)
    engine.runAndWait()
    engine.stop()

# Create a button to browse the file
button = tk.Button(master=frame2, text="Browse Files", command=browse, width=10, height=1)
button.grid(row=3, column=0)

# Choose whether male/female voice over
voice_label = tk.Label(master=frame2, text="Voice (Male/Female)", height=2)
voice_label.grid(row=0, column=0, sticky="w")

voice_over_entry = tk.Entry(master=frame2, width=15)
voice_over_entry.grid(row=0, column=1)

#add label for rate
rate_label = tk.Label(master=frame2, text="RATE", height=2)
rate_label.grid(row=1, column=0)

# Choose the rate
num = tk.Label(master=frame2, text="100", height=2)
num.grid(row=1, column=1)

def handle_dec():
    numd = int(num["text"])
    num["text"] = f"{numd - 10}"

def handle_inc():
    numi = int(num["text"])
    num["text"] = f"{numi + 10}"

dec = tk.Button(master=frame2, text="-", command=handle_dec)
dec.grid(row=2, column=0, sticky="nsew")

inc = tk.Button(master=frame2, text="+", command=handle_inc)
inc.grid(row=2, column=1, sticky="news")

window.mainloop()
