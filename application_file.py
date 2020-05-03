import tkinter as tk
import pandas as pd
from datagen import filegen
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from pandastable import Table
from algos import fcfs

#useful functions


def antt_display(dataframe):
    gantt_window = tk.Toplevel(root)
    gantt_window.title("Gantt Chart")
    gantt_window.geometry("500x400+600+200")
    cv = tk.Canvas(gantt_window)
    cv.pack()
    f = Figure(figsize=(5,5),dpi=100)
    a = f.add_subplot(111)
    a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
    canvas = FigureCanvasTkAgg(f)
    canvas.show()
    canvas.get_tk_widget().pack(side="bottom",fill="both",expand=True)

def gantt_display(dataframe):
    fig,gnt = plt.subplots()
    gnt.set_xlabel('Seconds Since Start')
    gnt.set_ylabel('Process ID')
    gnt.grid=True
    for i in range(dataframe.shape[0]):
        gnt.broken_barh([dataframe.iloc[i,4]-dataframe.iloc[i,2],dataframe.iloc[i,2]],(30, 9))
    plt.show()



def display_data(filename):
    for widget in mainFrame.winfo_children():
        widget.destroy()
    canvas_input = tk.Canvas(mainFrame)
    canvas_input.pack(fill="x",expand=1)
    df = pd.read_csv(filename)
    pt = Table(canvas_input,dataframe=df,showstatusbar=True)
    pt.show()

    def fcfs_func():
        button_frame.destroy()
        op_df = fcfs(filename)
        canvas_output = tk.Canvas(mainFrame)
        canvas_output.pack(fill="x",expand = 1)
        l = tk.Label(mainFrame,text="FCFS Scheduling")
        l.pack()
        output_table = Table(canvas_output,dataframe=op_df,showstatusbar=True)
        output_table.show()
        gantt_button_frame = tk.Frame(mainFrame)
        gantt_button_frame.pack()
        gantt_button = tk.Button(gantt_button_frame,text="Gantt Chart",command=lambda:gantt_display(op_df) )
        gantt_button.pack()
    button_frame=tk.Canvas(mainFrame)
    button_frame.pack()
    fcfs_button =tk.Button(button_frame,text="FCFS Scheduling",command = fcfs_func)
    sjf_button = tk.Button(button_frame, text="SJF Scheduling")
    priority_button = tk.Button(button_frame, text="Priority Scheduling")
    roundrobin_button = tk.Button(button_frame, text="RoundRobin Scheduling")
    fcfs_button.grid(row=0,column=0)
    sjf_button.grid(row=0,column=1)
    priority_button.grid(row=0,column=2)
    roundrobin_button.grid(row=0,column=3)


def open_function():
    file = tk.filedialog.askopenfile(initialdir="/")
    print()
    display_data(file.name)
def new_function():
    for widget in mainFrame.winfo_children():
        widget.destroy()
    datagenLabel = tk.LabelFrame(mainFrame,text="Make new random data")
    datagenLabel.pack(fill="x",expand="yes",side="top")
    #1
    l1 = tk.Label(datagenLabel,text="Number of processes")
    l1.grid(row=0,column=0)
    e1 = tk.Entry(datagenLabel,bd=5)
    e1.grid(row=0,column=1)
    #2
    l2 = tk.Label(datagenLabel, text="Max Burst Time")
    l2.grid(row=1,column=0)
    e2 = tk.Entry(datagenLabel, bd=5)
    e2.grid(row=1,column=1)
    #3
    l3 = tk.Label(datagenLabel, text="Min Burst Time")
    l3.grid(row=2, column=0)
    e3 = tk.Entry(datagenLabel, bd=5)
    e3.grid(row=2, column=1)
    #4
    l4 = tk.Label(datagenLabel, text="Average Interval Time")
    l4.grid(row=3, column=0)
    e4 = tk.Entry(datagenLabel, bd=5)
    e4.grid(row=3, column=1)
    #5
    l5 = tk.Label(datagenLabel, text="File name")
    l5.grid(row=4, column=0)
    e5 = tk.Entry(datagenLabel, bd=5)
    e5.grid(row=4, column=1)
    def file_is_made_window(filename):
        filewindow = tk.Toplevel(root)
        filewindow.geometry("+750+400")
        label = tk.Label(filewindow,text="File is Made!")
        label.pack()
        def new_data_display():
            filewindow.destroy()
            datagenLabel.destroy()
            display_data(r"./CPU-Scheduler-Python/Random_data/"+filename + ".csv")
        button1 = tk.Button(filewindow, text="Display file?",command=new_data_display)
        button1.pack()
        button2 = tk.Button(filewindow, text="Close",command=filewindow.destroy)
        button2.pack()
    def enterInfo():
        num = int(e1.get())
        max_burst = int(e2.get())
        min_burst = int(e3.get())
        avg_time = int(e4.get())
        filename = e5.get()
        filegen(num,max_burst,min_burst,avg_time,filename)
        file_is_made_window(filename)
    def cancelInfo():
        datagenLabel.destroy()
    fileCreateButton = tk.Button(datagenLabel,command=cancelInfo,text="Cancel")
    fileCreateButton.grid(row=5,column=0)
    fileCreateButton = tk.Button(datagenLabel, command=enterInfo, text="Create File")
    fileCreateButton.grid(row=5,column=1)

    
def exit_function():
    root.destroy()


#app starts
root = tk.Tk()
root.title("CPU Scheduler")
root.geometry("500x400+700+300")
menubar = tk.Menu(root) #Menu starts

#filemenu
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New",command=new_function)
filemenu.add_command(label="Open",command=open_function)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=exit_function)
menubar.add_cascade(label="File",menu=filemenu)

#helpmenu
helpmenu = tk.Menu(menubar,tearoff = 0)
helpmenu.add_command(label="Read Here")
menubar.add_cascade(label="Help",menu=helpmenu)

root.config(menu=menubar) #Menu Ends

mainFrame = tk.Frame(root,bd=4,bg="#D3D3D3")
mainFrame.pack(fill="both",expand="yes")
mainCanvas = tk.Canvas(mainFrame)
left = tk.Label(root,text="CPU Scheduling Simulation")
left.pack()
root.mainloop()

