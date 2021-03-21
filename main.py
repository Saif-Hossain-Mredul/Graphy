from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import messagebox
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import pchip
from collections import OrderedDict

global data_list

data_list = []


class Data():

    def __init__(self, x, y, ls_radio_but, gs_radio_but, label):
        self.x = x
        self.y = y
        self.ls_radio_but = ls_radio_but
        self.gs_radio_but = gs_radio_but
        self.label = label

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_ls_rad_but(self):
        return self.ls_radio_but

    def get_gs_rad_but(self):
        return self.gs_radio_but

    def get_label(self):
        return self.label


def popup(message):
    messagebox.showinfo("Graphy", message)


def conv_list(list):
    new_list = []

    try:
        for element in list:
            new_list.append(int(element))

        return new_list

    except ValueError:
        popup("Please enter X and Y values")


# function for collecting radiobutton response
def ls_radio_selct():
    global ls_radio_but

    if ls_var.get() == 1:
        ls_radio_but = '-'

    else:
        ls_radio_but = '--'


# function for collecting graph style radiobutton response
def gs_radio_selct():
    global gs_radio_but

    gs_radio_but = gs_var.get()


# function for showing temporary figure
def temp_graph(x, y, linestyle, graphstyle, title, x_name, y_name, line_name):
    if graphstyle == 1:
        plt.close()

        # changes the figure window icon
        plt.Figure()
        thismanager = plt.get_current_fig_manager()
        thismanager.window.wm_iconbitmap("images\\icon_1.ico")

        plt.style.use('seaborn')
        # plt.scatter(x, y)
        plt.plot(x, y, 'o-', linestyle=linestyle, label=line_name)
        plt.title(str(title))
        plt.xlabel(str(x_name))
        plt.ylabel(str(y_name))
        plt.legend()
        plt.show()

    elif graphstyle == 2:
        plt.close()

        pch = pchip(x, y)
        x_smooth = np.linspace(x[0], x[-1], 100)  # evenly creates 100 plot between min an max
        y_smooth = pch(x_smooth)

        # changes the figure window icon
        plt.Figure()
        thismanager = plt.get_current_fig_manager()
        thismanager.window.wm_iconbitmap("images\\icon_1.ico")

        plt.style.use('seaborn')
        plt.scatter(x, y)
        plt.plot(x_smooth, y_smooth, label=line_name)
        plt.title(str(title))
        plt.xlabel(str(x_name))
        plt.ylabel(str(y_name))
        plt.legend()
        plt.show()

    else:
        plt.close()

        denominator = x.dot(x) - x.mean() * x.sum()
        m = (x.dot(y) - y.mean() * x.sum()) / denominator
        b = (y.mean() * x.dot(x) - x.mean() * x.dot(y)) / denominator
        line = m * x + b

        # changes the figure window icon
        plt.Figure()
        thismanager = plt.get_current_fig_manager()
        thismanager.window.wm_iconbitmap("images\\icon_1.ico")

        plt.style.use('seaborn')
        plt.scatter(x, y)
        plt.plot(x, line, label=line_name)
        plt.title(str(title))
        plt.xlabel(str(x_name))
        plt.ylabel(str(y_name))
        plt.legend()
        plt.show()


# function for showing main figure
def main_graph():
    try:
        plt.clf()
        for temp in data_list:
            x = temp.x
            y = temp.y

            if temp.gs_radio_but == 1:

                plt.Figure()
                thismanager = plt.get_current_fig_manager()
                thismanager.window.wm_iconbitmap("images\\ icon_1.ico")

                plt.style.use('seaborn')
                plt.plot(x, y, 'o-', label=temp.label)

            elif temp.gs_radio_but == 2:

                pch = pchip(x, y)
                x_smooth = np.linspace(x[0], x[-1], 100)  # evenly creates 100 plot between min an max
                y_smooth = pch(x_smooth)

                # changes the figure window icon
                plt.Figure()
                thismanager = plt.get_current_fig_manager()
                thismanager.window.wm_iconbitmap("images\\icon_1.ico")

                plt.style.use('seaborn')
                plt.scatter(x, y)
                plt.plot(x_smooth, y_smooth, label=temp.label)

            else:

                denominator = x.dot(x) - x.mean() * x.sum()
                m = (x.dot(y) - y.mean() * x.sum()) / denominator
                b = (y.mean() * x.dot(x) - x.mean() * x.dot(y)) / denominator
                line = m * x + b

                # changes the figure window icon
                plt.Figure()
                thismanager = plt.get_current_fig_manager()
                thismanager.window.wm_iconbitmap("images\\icon_1.ico")

                plt.style.use('seaborn')
                plt.scatter(x, y)
                plt.plot(x, line, label=temp.label)

        plt.title(str(title))
        plt.xlabel(str(x_name))
        plt.ylabel(str(y_name))
        plt.legend()
        plt.show()

    except ValueError:
        popup("Please enter X and Y values")


# Function for collecting graph data
def graph_data():
    global x
    global y
    global title
    global x_name
    global y_name
    global line_name
    global cb_var
    global data_list

    # graph points from entries
    list_x = entry_x.get().split(",")
    list_y = entry_y.get().split(",")

    # converting list to numpy array
    x = np.array(sorted(conv_list(list_x)))
    y = np.array(conv_list(list_y))

    # graph title
    title = entry_title.get()

    # data for both axis label
    x_name = entry_x_axis_name.get()
    y_name = entry_y_axis_name.get()

    # name of line
    line_name = entry_line_name.get()

    # check box data for y value update
    cb_var = checkVar.get()

    """
    if the box is not ticked, then a temporary figure will popup
    if the box is ticked, then the main figure will popup.
    """

    if cb_var == 0:
        try:
            temp_graph(x, y, ls_radio_but, gs_radio_but, title, x_name, y_name, line_name)

        except NameError:
            popup("Please select Line style and Graph style")

        except ValueError:
            popup("Enter X and Y values correctly")

    else:
        num = Data(x, y, ls_radio_but, gs_radio_but, line_name)
        data_list.append(num)

        """loop for checking if the coordinate value already exists or not"""

        i = 0
        for temp in data_list:
            if list(temp.x) == list(num.x) and list(temp.y) == list(num.y):
                data_list[i] = num

            else:
                data_list.append(num)

            i += 1

        popup("Saved to main figure")

    data_list = list(OrderedDict.fromkeys(data_list))
    checkVar.set(0)
    print(data_list)


# """Main window start""" #

root = ThemedTk(theme="breeze")
root.title('Graphy')
root.iconbitmap(r'images\icon_1.ico')

root.geometry('650x500')
root.resizable(width=False, height=False)

# creating upper frame
upper_frame = ttk.Frame(root)
upper_frame.place(relwidth=1, relheight=0.3)

x_label = ttk.Label(upper_frame, text='X values : ')
x_label.place(x=35, rely=0.2)

entry_x = ttk.Entry(upper_frame)
entry_x.place(x=100, rely=0.17, relwidth=0.75, height=30)

y_label = ttk.Label(upper_frame, text='Y values : ')
y_label.place(x=35, rely=0.60)

entry_y = ttk.Entry(upper_frame)
entry_y.place(x=100, rely=0.58, relwidth=0.75, height=30)

# creating middle left frame
middle_left_frame = ttk.Frame(root)
middle_left_frame.place(rely=0.3, relwidth=0.5, relheight=0.55)

# Labels
title = ttk.Label(middle_left_frame, text='Graph title : ')
title.grid(column=0, row=0, pady=7, padx=35, sticky='nw')

x_axis_name = ttk.Label(middle_left_frame, text='X axis name : ')
x_axis_name.grid(column=0, row=1, pady=7, padx=35, sticky='nw')

y_axis_name = ttk.Label(middle_left_frame, text='Y axis name : ')
y_axis_name.grid(column=0, row=2, pady=7, padx=35, sticky='nw')

line_name_label = ttk.Label(middle_left_frame, text='Line name : ')
line_name_label.grid(column=0, row=3, pady=7, padx=35, sticky='nw')

# Entries
entry_title = ttk.Entry(middle_left_frame)
entry_title.grid(column=1, row=0, pady=5)

entry_x_axis_name = ttk.Entry(middle_left_frame)
entry_x_axis_name.grid(column=1, row=1, pady=5)

entry_y_axis_name = ttk.Entry(middle_left_frame)
entry_y_axis_name.grid(column=1, row=2, pady=5)

entry_line_name = ttk.Entry(middle_left_frame)
entry_line_name.grid(column=1, row=3, pady=5)

# creating middle right frame
middle_right_frame = ttk.Frame(root)
middle_right_frame.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.55)

# line style label and Radio buttons

ls_var = tk.IntVar()  # line style radio button variable

# label
line_style_label = ttk.Label(middle_right_frame, text='Line style  : ')
line_style_label.grid(column=1, row=1, sticky='nw')

# line style radio buttons
line_style1 = ttk.Radiobutton(middle_right_frame, variable=ls_var, value=1,
                              command=lambda: ls_radio_selct())
img1 = tk.PhotoImage(file="images\\line_style1.png")
line_style1.config(image=img1)
line_style1.grid(column=3, row=2)

line_style2 = ttk.Radiobutton(middle_right_frame, variable=ls_var, value=2,
                              command=lambda: ls_radio_selct())
img2 = tk.PhotoImage(file="images\\line_style2.png")
line_style2.config(image=img2)
line_style2.grid(column=3, row=3)

# Graph style label and radio buttons

gs_var = tk.IntVar()  # graph style radio button variable

# label
graph_style_label = ttk.Label(middle_right_frame, text='Graph style  : ')
graph_style_label.grid(column=1, row=4, sticky='nw')

# radio buttons
graph_style1 = ttk.Radiobutton(middle_right_frame, text='Accurate', variable=gs_var, value=1,
                               command=lambda: gs_radio_selct())
graph_style1.grid(column=3, row=5, sticky='nw')

graph_style2 = ttk.Radiobutton(middle_right_frame, text='Smooth', variable=gs_var, value=2,
                               command=lambda: gs_radio_selct())
graph_style2.grid(column=3, row=6, sticky='nw')

graph_style3 = ttk.Radiobutton(middle_right_frame, text='Best fit', variable=gs_var, value=3,
                               command=lambda: gs_radio_selct())
graph_style3.grid(column=3, row=7, sticky='nw')

# check button
checkVar = tk.IntVar()
remove_value = ttk.Checkbutton(middle_right_frame, text="Save to main \nfigure", variable=checkVar)
remove_value.grid(column=1, row=8)

# creating lower frame
lower_frame = ttk.Frame(root)
lower_frame.place(rely=0.85, relwidth=1, relheight=0.15)

view_main_figure = ttk.Button(lower_frame, text='View main figure',  # view main figure button
                              command=lambda: main_graph())
view_main_figure.pack(side='left', anchor='n', padx=75, pady=0)

submit = ttk.Button(lower_frame, text='Submit',  # submit button
                    command=lambda: [graph_data()])
submit.pack(side='right', anchor='n', padx=128)

root.mainloop()
