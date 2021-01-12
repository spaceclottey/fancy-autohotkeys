
# Thread Rambler 1.0
# Written by TheTrueSquiward, idea by Raj. 

# # Upcoming
# Email Capabilities


# # Possible Additions
# Priority sorting
# instant addition to supermemo mail collection 
# shortcut to open it built in (rather than using ahk)
# show all used threads rather than having to remember



import tkinter as tk
import random

threadsFile = open('threads.txt', 'r')
threadsList = threadsFile.readlines()
win_reviewThreads = 0
i = 0


# Windows
# Capture Thread Window
# thread review
# filter by tags
# start thread review



    
# Functions

def next_thread(filteredThreads, ent_currentThread):
    global i
    if i >= len(filteredThreads):
        i = 0
    
    currentThread = filteredThreads[i]
    currentThreadLabel = tk.Label(text=currentThread)

    ent_currentThread.delete(0, tk.END)
    ent_currentThread.insert(0, currentThread)
    
    
    if i < len(filteredThreads):
        i += 1


     
def filter_threads(tags):
    global win_reviewThreads

    filteredThreads = []
    splitTags = tags.split(' ')

    for thread in threadsList: #Filters all the threads for the ones that match the tags given
        for tag in splitTags:
            if tag in thread:
                threadMatch = True
            else:
                threadMatch = False
        if threadMatch == True:
            filteredThreads.append(thread)
    
    random.shuffle(filteredThreads)

    # Create Thread Review Window
    lbl_threadReview = tk.Label(win_reviewThreads, text="Thread Review")
    lbl_threadReview.pack()

    ent_currentThread = tk.Entry(win_reviewThreads, width=100)
    ent_currentThread.pack()
    
    nextThreadButton = tk.Button(win_reviewThreads, text="Next Thread", command= lambda: next_thread(filteredThreads, ent_currentThread))
    nextThreadButton.pack()

    btn_mailThread= tk.Button(win_reviewThreads, text="Mail Thread", command=next_thread)
    btn_mailThread.pack()
    


def review_threads():
    global win_reviewThreads
    
    # Create new window for thread review
    win_reviewThreads = tk.Toplevel()
    win_reviewThreads.title("Review threads")

    # Create new window elements

    # Which tags do you want to review? (leave blank for none)
    lbl_reviewTags = tk.Label(win_reviewThreads, text="Enter the tag you want to review (leave blank to review all threads)")
    lbl_reviewTags.pack()

    ent_reviewTags = tk.Entry(win_reviewThreads)
    ent_reviewTags.pack()

    btn_reviewTags = tk.Button( win_reviewThreads, text="Confirm these Tags", command= lambda: filter_threads(ent_reviewTags.get()))
    btn_reviewTags.pack()



def submit_thread():
    thread = ent_enterThread.get()
    tags = ent_addTags.get()
    if thread != '':
        threadsFile = open('threads.txt', 'a')
        threadsFile.write(thread + ',' + tags + '\n')
        threadsFile.close()
        ent_enterThread.delete(0, tk.END)
        ent_addTags.delete(0, tk.END)
    return



# Capture Thread Window - creation

win_CaptureThread = tk.Tk()  
win_CaptureThread.geometry("200x150") 
win_CaptureThread.title("Capture Thread")   



# Capture Thread Window - add widgets

lbl_enterThread = tk.Label(win_CaptureThread, text="Enter Thread")  #'Enter Thread' Label
lbl_enterThread.pack()

ent_enterThread = tk.Entry() #Enter Thread text box
ent_enterThread.pack()

lbl_addTags = tk.Label(win_CaptureThread, text='Add Tags')  #Add Tags label
lbl_addTags.pack()

ent_addTags = tk.Entry(win_CaptureThread) #Add tags textbox
ent_addTags.pack()

btn_submitThread = tk.Button(win_CaptureThread, text="Submit", command=submit_thread) # Submit button
btn_submitThread.pack()

btn_reviewThreads = tk.Button(win_CaptureThread, text="Review Threads", command=review_threads) # Review Threads button
btn_reviewThreads.pack()



# Mainloop

win_CaptureThread.mainloop()
