import tkinter as tk
from tkinter import ttk

import ctypes
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )

#finestra
root = tk.Tk()
larghezza = 500
altezza = 600
# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# find the center point
center_x = int(screen_width/2 - larghezza / 2)
center_y = int(screen_height/2 - altezza / 2)
# set the position of the window to the center of the screen
root.geometry(f'{larghezza}x{altezza}+{center_x}+{center_y}')
root.title('TO-DO CRISP!')
root.attributes('-alpha',0.95)
root.iconbitmap('datiProgramma/icona.ico')
root.resizable(False, True)

root.attributes('-topmost',True)

#stile
ttk.Style().theme_use('xpnative')
#inizio
welcomeLabel = ttk.Label(root, text='inserisci attività e premi enter')
welcomeLabel.pack()
welcomeText = tk.Text(root, height=1, width=55)
welcomeText.pack()

currentTaskList = []

#crea l'attività quando inizia il programma
def createTask(task):
	f = ttk.Frame(root)
	f.rowconfigure(0, weight=1)
	f.columnconfigure(0, weight=1)
	f.columnconfigure(1, weight=1)
	f.pack()

	textToRemove=task

	def delete():
		f.destroy()
		currentTaskList.remove(textToRemove)

	taskLabel = ttk.Label(f, text=task, width=50, wraplengt=200)
	taskLabel.grid(row=0, column=0, padx=(27,0))
	taskButton = ttk.Button(f, text='elimina', command=delete, width=30)
	taskButton.grid(row=0, column=1, padx=27)

file = open('datiProgramma/salvataggi.txt', 'r')
for i in file:
	i = i.strip('\n')
	createTask(i)
	currentTaskList.append(i)

#crea l'attività quando clicchi enter
def createTask():

	global welcomeText

	f = ttk.Frame(root)
	f.rowconfigure(0, weight=1)
	f.columnconfigure(0, weight=1)
	f.columnconfigure(1, weight=1)
	f.pack()

	def delete():
		f.destroy()
		currentTaskList.remove(textToRemove)

	returnedText = welcomeText.get('1.0', 'end-2c')
	currentTaskList.append(returnedText)
	textToRemove=returnedText
	welcomeText.delete('1.0', 'end')

	taskLabel = ttk.Label(f, text=returnedText, width=50, wraplengt=200)
	taskLabel.grid(row=0, column=0, padx=(27,0))
	taskButton = ttk.Button(f, text='elimina', command=delete, width=30)
	taskButton.grid(row=0, column=1, padx=27)

def whenPressedEnter(event):
	createTask()

root.bind('<Return>', whenPressedEnter)

root.mainloop()
print(currentTaskList)

#aggiorna i salvataggi
file = open('datiProgramma/salvataggi.txt','w')
file.truncate(0)

for i in currentTaskList:
	savedActivity = i + '\n'
	file.write(savedActivity)
file.close()