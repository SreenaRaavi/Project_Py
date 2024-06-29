import pygame
from pygame.locals import *
import pyttsx3
from PyPDF2 import PdfReader

pygame.init()

canvas = pygame.display.set_mode((700, 500))
pygame.display.set_caption("PDF to Audio Reader")

bg_color = (179, 158, 181)

title = pygame.image.load("..\\images\\Audiobook.png")
heart = pygame.image.load("..\\images\\heart.png")
campfire = pygame.image.load("..\\images\\campfire.png")
crow = pygame.image.load("..\\images\\crow.png")
donkey = pygame.image.load("..\\images\\donkey.png")
elephant = pygame.image.load("..\\images\\elephant.png")
lion = pygame.image.load("..\\images\\lion.png")
potion = pygame.image.load("..\\images\\potion.png")
school = pygame.image.load("..\\images\\school.png")
tree = pygame.image.load("..\\images\\tree.png")

images = [campfire, crow, donkey, elephant, lion, potion, school, tree]

pygame.display.set_icon(heart)

campfire_pdf = "..\\pdf\\Campfire.pdf"
crow_pdf = "..\\pdf\\Crow.pdf"
donkey_pdf = "..\\pdf\\Donkey.pdf"
elephant_pdf = "..\\pdf\\Elephant.pdf"
lion_pdf = "..\\pdf\\Lion.pdf"
potion_pdf = "..\\pdf\\Potion.pdf"
school_pdf = "..\\pdf\\School.pdf"
tree_pdf = "..\\pdf\\Tree.pdf"

pdfs = [campfire_pdf, crow_pdf, donkey_pdf, elephant_pdf, lion_pdf, potion_pdf, school_pdf, tree_pdf]

positions = [
    (50, 180),  # campfire
    (350, 350), # crow
    (350, 180), # donkey
    (50, 350),  # elephant
    (200, 180), # lion
    (500, 180), # potion
    (500, 350), # school
    (200, 350)  # tree
]

click_on_box = pygame.USEREVENT + 1

def audio(file):
    reader = PdfReader(file)
    no_of_pages = len(reader.pages)

    parts = []

    for i in range(no_of_pages):
        page = reader.pages[i]
        text = page.extract_text()
        parts.append(text)

    full_text = " ".join(parts)

    engine = pyttsx3.init()
    engine.setProperty('rate', 175)
    engine.setProperty('volume', 1)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say("Hello, this is the children version of AudioBook")
    engine.say(full_text)
    engine.say("Yup! We are done with the story. Bye Bye")

    engine.runAndWait()
    engine.stop()

while True:
    canvas.fill(bg_color)
    canvas.blit(title, (50, 30))

    for image, pos in zip(images, positions):
        canvas.blit(image, pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == MOUSEBUTTONDOWN:
            for ind, (image, pos) in enumerate(zip(images, positions)):
                image_rect = image.get_rect(topleft=pos)
                if image_rect.collidepoint(event.pos):
                    pdf = pdfs[ind]
                    audio(pdf)

    pygame.display.update()
