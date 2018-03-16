import tkinter
from tkinter import *
# import tkFileDialog
from tkinter import filedialog
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import seaborn as sns


    #a = Button(text="Center Button")
    #a.place(relx=5, rely=.5, anchor=CENTER)
    #mainloop






if __name__ == '__main__':
    form = tkinter.Tk()

    getFld = tkinter.IntVar()

    form.wm_title('SRUTool')

    stepOne = tkinter.LabelFrame(form, text=" 1. Add ISR File Details: ")
    stepOne.grid(row=0, columnspan=7, sticky='W', \
                 padx=5, pady=5, ipadx=5, ipady=5)

    helpLf = tkinter.LabelFrame(form, text=" Quick Help ")
    helpLf.grid(row=0, column=9, columnspan=2, rowspan=8, \
                sticky='NS', padx=5, pady=5)
    helpLbl = tkinter.Label(helpLf, text="Help is coming soon.")
    helpLbl.grid(row=0)

    stepTwo = tkinter.LabelFrame(form, text=" 2. Enter Stat Details: ")
    stepTwo.grid(row=2, columnspan=7, sticky='W', \
                 padx=40, pady=40, ipadx=40, ipady=20)

    stepThree = tkinter.LabelFrame(form, text=" 3. Configure: ")
    stepThree.grid(row=3, columnspan=7, sticky='W', \
                   padx=5, pady=5, ipadx=5, ipady=5)


    #mainloop
   
    #Step 1
    inFileLbl = tkinter.Label(stepOne, text="Select ISR File:")
    inFileLbl.grid(row=0, column=0, sticky='E', padx=5, pady=2)

    inFileTxt = tkinter.Entry(stepOne)
    inFileTxt.grid(row=0, column=1, columnspan=7, sticky="WE", pady=3)

    def callback():
        fileName = filedialog.askopenfilename()
        inFileTxt.insert(0, fileName)

    inFileBtn = tkinter.Button(stepOne, text="Browse ...", command=callback)
    inFileBtn.grid(row=0, column=8, sticky='W', padx=5, pady=2)

    outFileLbl = tkinter.Label(stepOne, text="Save File to:")
    outFileLbl.grid(row=1, column=0, sticky='E', padx=5, pady=2)

    outFileTxt = tkinter.Entry(stepOne)
    outFileTxt.grid(row=1, column=1, columnspan=7, sticky="WE", pady=2)

    def outfile_callback():
        fileName = filedialog.asksaveasfilename()
        outFileTxt.insert(0, fileName)

    def execute_callback():
       data = pd.read_csv(inFileTxt.get())
       ax = sns.barplot(data=data, x='Sprint', y='Results', hue='Status')
       fig = ax.get_figure()
       fig.savefig(outFileTxt.get())
    #Button
    a = Button(text="Execute!!", command=execute_callback)
    a.place(relx=.7, rely=.08, anchor=CENTER)

    outFileBtn = tkinter.Button(stepOne, text="Browse ...", command=outfile_callback)
    outFileBtn.grid(row=1, column=8, sticky='W', padx=5, pady=2)


    #Step 2
    outTblLbl = tkinter.Label(stepTwo, \
          text="Enter the Title to be used in the bargraph:")
    outTblLbl.grid(row=3, column=0, sticky='W', padx=5, pady=2)

    outTblTxt = tkinter.Entry(stepTwo)
    outTblTxt.grid(row=3, column=1, columnspan=3, pady=2, sticky='WE')

    fldLbl = tkinter.Label(stepTwo, \
                           text="Enter Committed Values:")
    fldLbl.grid(row=4, column=0, padx=5, pady=2, sticky='W')

    getFldChk = tkinter.Checkbutton(stepTwo, \
                           text="Get fields automatically from CSV file",\
                           onvalue=1, offvalue=0)
    getFldChk.grid(row=4, column=1, columnspan=3, pady=2, sticky='WE')
    
    fldRowTxt = tkinter.Entry(stepTwo)
    fldRowTxt.grid(row=5, columnspan=5, padx=5, pady=2, sticky='WE')

    #Y-axis
    fldLbl = tkinter.Label(stepTwo, \
                           text="Enter Delivered Values:")
    fldLbl.grid(row=6, column=0, padx=5, pady=2, sticky='W') #For text

    getFldChk = tkinter.Checkbutton(stepTwo, \
                           text="Get fields automatically from CSV file",\
                           onvalue=1, offvalue=0)
    getFldChk.grid(row=6, column=1, columnspan=3, pady=2, sticky='WE')

    fldRowTxt = tkinter.Entry(stepTwo)
    fldRowTxt.grid(row=7, columnspan=5, padx=5, pady=2, sticky='WE') #Entry
    

    #Step 3
    transChk = tkinter.Checkbutton(stepThree, \
               text="Enable Transaction", onvalue=1, offvalue=0)
    transChk.grid(row=6, sticky='W', padx=5, pady=2)

    transRwLbl = tkinter.Label(stepThree, \
                 text=" => Specify number of rows per transaction:")
    transRwLbl.grid(row=6, column=2, columnspan=2, \
                    sticky='W', padx=5, pady=2)

    transRwTxt = tkinter.Entry(stepThree)
    transRwTxt.grid(row=6, column=4, sticky='WE')

    form.mainloop()

    
