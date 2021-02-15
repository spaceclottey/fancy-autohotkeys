

# == Thread Rambler 2.0 ==
# Written by TheTrueSquiward, idea by Raj. 

# == Instructions ==
# Run 'pip install keyboard' at command prompt (takes about 5 seconds)
# Press ctrl+period to open the thread capturing window


# # Upcoming
# Email Capabilities
# # Possible Additions
# Priority sorting
# instant addition to supermemo mail collection 

# show all used tags rather than having to remember



import tkinter as tk
import random
import keyboard

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
    
    print(i)
    print(filteredThreads)
    currentThread = filteredThreads[i]

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



## == Capture Thread Window - add widgets ==


#'Enter Thread' Label
lbl_enterThread = tk.Label(win_CaptureThread, text="Enter Thread")  
lbl_enterThread.pack()

#Enter Thread text box
ent_enterThread = tk.Entry() 
ent_enterThread.pack()

#Add Tags label
lbl_addTags = tk.Label(win_CaptureThread, text='Add Tags')  
lbl_addTags.pack()

#Add tags textbox
ent_addTags = tk.Entry(win_CaptureThread) 
ent_addTags.pack()

#Submit button
btn_submitThread = tk.Button(win_CaptureThread, text="Submit", command=submit_thread)
btn_submitThread.pack()

#Review Threads button
btn_reviewThreads = tk.Button(win_CaptureThread, text="Review Threads", command=review_threads) 
btn_reviewThreads.pack()


windowVisible = True


def show_window():
    global windowVisible
    if windowVisible == True:
        win_CaptureThread.withdraw()
        print("hiding window!")
        windowVisible = False

    elif windowVisible == False:
        win_CaptureThread.deiconify()
        print("showing window!")
        windowVisible = True





keyboard.add_hotkey('ctrl+.', show_window, args=())


# # Mainloop

win_CaptureThread.mainloop()


