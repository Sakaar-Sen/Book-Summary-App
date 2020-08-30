from tkinter import *
from selenium import webdriver
from tkinter import messagebox
from selenium.webdriver.chrome.options import Options  
import os
import random
from selenium import webdriver


def start():
    global listOfAllbooks
    global driver
    #chrome_options = Options()
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome( executable_path = r"C:\Users\Sakaar\Desktop\vs_Python\BookSummary App\driver\chromedriver.exe")



def choose():
    global selected_book
    global e
    global get_title
    e = True
    while e:
        
        driver.get("http://www.wikisummaries.org/w/index.php?title=Special:PopularPages&limit=100")
        box_area = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/ol')
        listOfAllbooks = box_area.find_elements_by_tag_name('a')
        selected_book = random.choice(listOfAllbooks)
        selected_book.click()
        get_title = driver.title

        response = messagebox.askyesnocancel(str(get_title), 'Do you want to save this summary?')
        if response == True:
            saveFile()
            messagebox.showinfo("Success", "File succesfully saved.")
            break

        elif response == False:
            e = True

        elif response is None:
            break


def saveFile():
    allParas = driver.find_elements_by_xpath('//*[@id="mw-content-text"]')
    with open((get_title + ".txt"), "w") as file:    
        for para in allParas:
            file.write(para.text)

start()
master = Tk()
master.title("v1.0.0")
label1 = Label(master, text = "Book Summary App", font=("Times New Roman", 30, "bold")).grid(row = 0, column = 0, padx = 10, pady = 15, ipadx = 10, ipady = 20)
button1 = Button(master, text = "Click here to get started", command = choose).grid(row = 1, column = 0, ipadx = 10, ipady =10, pady = 20, columnspan= 2)
label2 = Label(master, text = "*loading might take a while", font=("Helvetica", 10, )).grid(row = 3, column = 0, padx = 10, ipadx = 10)


master.mainloop()





