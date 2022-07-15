from tkinter import *
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle

loaded_model = pickle.load(open('parkinsons_model', 'rb'))

root = Tk()
root.geometry("500x300")
root.title("Parkinson's Disease Detection")

def Predict(arr):
    input_data = np.asarray(arr)
    input_data_reshape = input_data.reshape(1, -1)
    scaler = StandardScaler()
    scaler.fit(input_data_reshape)
    std_data = scaler.transform(input_data_reshape)
    predict = loaded_model.predict(std_data)
    return predict[0]


def Get_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    print(INPUT)
    lis = INPUT.split(',')
    lis1 = [float(s) for s in lis]
    print(lis1)
    x = Predict(lis1)
    if x == 0:
        Output.insert(END, "The Person does not have Parkinson's Disease")
        print("The Person does not have Parkinson's Disease")
    else:
        Output.insert(END, "The Person has Parkinson's Disease")
        print("The Person has Parkinson's")


l = Label(text="Enter comma Separated values")
inputtxt = Text(root, height=10, width=50, bg="light cyan")
Output = Text(root, height=5, width=25, bg="light grey")

Display = Button(root, height=2, width=20, text="Show", command=Get_input)

l.pack()
inputtxt.pack()
Display.pack()
Output.pack()

mainloop()
