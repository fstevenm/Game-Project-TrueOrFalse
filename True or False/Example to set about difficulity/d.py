import sols
import tkinter
def a():
    sols.easy()
    
a()
root=tkinter.Tk()

tkinter.Button(root,command=a).pack()
root.mainloop()