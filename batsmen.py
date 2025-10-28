import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk,filedialog,Button
import numpy as np
root=Tk()
root.title("Batsmen Performance Graph Generator" )
def browse_file():
    file_path=filedialog.askopenfilename(filetypes=[("csv Files","*.csv"),("Excel Files","*.xlsx")])
    if file_path:
        generate_graph(file_path)
def generate_graph(file_path):
        data=pd.read_csv(file_path)
        batsmen_names=data.iloc[:,0]
        years=data.columns[1:]
        bar_width=0.15
        plt.figure(figsize=(10,6))
        for i,batsman_name in enumerate(batsmen_names):
            plt.bar(np.arange(len(years))+i*bar_width,data.iloc[i,1:],bar_width,label=batsman_name)
        plt.xlabel('year')
        plt.ylabel('Performance Score')
        plt.title('Batsmen Performance Over Years')
        plt.xticks(np.arange(len(years))+0.5,years)
        plt.legend()
        plt.show()
browse_button=Button(root,text="Browse CSV File",command=browse_file)
browse_button.pack(pady=10)
root.mainloop()
