from Tkinter import *

master = Tk()

canvas_width=800
canvas_height=master.winfo_screenheight() - 100
canvas=Canvas(master, width = canvas_width, height=canvas_height)
#topx, topy, bottomx, bottomy
#top left corner = 0,0
canvas.create_oval(canvas_width/16, 10, (11*canvas_width)/16, canvas_height-10, fill="green", width=2)
canvas.create_oval((5*canvas_width)/16, 10, (15*canvas_width/16), canvas_height-10, outline="blue", fill="orange", width=2)
canvas.create_oval(canvas_width/16, 10, (11*canvas_width)/16, canvas_height-10, outline="red", width=2)


canvas.pack()

mainloop()
print "Exited successfully"
