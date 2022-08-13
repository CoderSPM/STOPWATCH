
import tkinter as tk
class stopwatch(tk.Frame):
    def __init__(self,window=None):
        super().__init__(window)
        self.window=window
        self.new_time=''
        self.running=False
        self.total_hours=0
        self.total_minutes=0
        self.total_seconds=0
        self.pack()
        self.features()

    def features(self):
        self.stopwatch_label=tk.Label(self,text='00:00:00',backgroung='black',foreground='white',font=('arial',85,"bold"))
        self.stopwatch_label.pack()

        self.start_time_button=tk.Button(self,text="START",height=5,width=7,font=('arial',18,"bold"),background="green")
        self.start_time_button.pack(side=tk.LEFT)

        self.stop_time_button=tk.Button(self,text="STOP",height=5,width=7,font=('arial',18,"bold"),background="red")
        self.start_time_button(side=tk.LEFT)

        self.reset_time_button = tk.Button(self, text="RESET", height=5, width=7, font=('arial', 18, "bold"),background="yellow")
        self.reset_time_button(side=tk.LEFT)



root=tk.Tk()
obj=stopwatch(window=root)
obj.mainloop()


