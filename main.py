import tkinter as tk
from tkinter import ttk

global_data = [25, 50, 75, 100, 50, 75, 100, 10, 21, 1, 2, 3, 0]
def bubble_sort(canvas, arr):
    def sort_step(i, j):
        if i < len(arr):
            if j < len(arr) - i - 1:
                # Swap elements if needed
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Update the canvas
                draw_bar_chart(canvas, arr)
                # Schedule the next comparison
                canvas.after(100, sort_step, i, j + 1)
            else:
                # Move to the next pass
                canvas.after(100, sort_step, i + 1, 0)
        else:
            # Sorting is complete
            draw_bar_chart(canvas, arr)

    # Start the sorting process
    sort_step(0, 0)
def draw_bar_chart(canvas, data, width=700, height=500):
    # Clear the canvas
    canvas.delete("all")

    # Dimensions
    margin = 20
    bar_width = (width - 2 * margin) / len(data) - 10
    max_value = max(data)

    # Draw bars
    for i, value in enumerate(data):
        x1 = margin + i * (bar_width + 10)
        y1 = height - margin
        x2 = x1 + bar_width
        y2 = height - margin - (value / max_value * (height - 2 * margin))

        canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="black")
        canvas.create_text((x1 + x2) / 2, y1 + 10, text=str(value), anchor="n")

# Update the bar chart to display current input
def update(event, canvas, entry):
    string = entry.get()

    if(string.endswith(',') == False):
        # Split the string by commas
        string_list = string.split(',')
        global global_data
        global_data = list(map(int, string_list))
        draw_bar_chart(canvas, global_data)

def select_sort(canvas, option):
    global global_data
    if(option == "Bubble Sort"):
        bubble_sort(canvas, global_data)

def main():
    root = tk.Tk()
    root.title("Sorting Visualizer")

    # Label widget input
    label = tk.Label(root,text="Enter Value (Numbers separated by commas): ")
    label.grid(row=1, column=0, sticky="W", padx=10)

    # Setting default value
    global global_data
    default = (','.join(str(s) for s in global_data))
    text = tk.StringVar()
    text.set(default)
    # Entry widget
    entry = tk.Entry(root, width=70, textvariable=text)
    entry.grid(row=1, column=0, sticky="E", padx=10)

    # Dropdown menu to select type of sort
    sort_option = ('Bubble Sort', 'Other')
    sort_chosen = ttk.Combobox(root, width=27, values=sort_option)
    sort_chosen.grid(row=0, column=0)
    # Set default to Bubble Sort
    sort_chosen.current(0)

    # Canvas Widget
    canvas = tk.Canvas(root, width=700, height=500, bg="white")
    canvas.grid(row=2, column=0)

    # Button to start sort
    button = tk.Button(root, text="Sort", command=lambda: select_sort(canvas, sort_chosen.get()))
    button.grid(row=3,column=0)

    root.bind("<KeyPress>", lambda event: update(event, canvas, entry))

    draw_bar_chart(canvas, global_data)

    root.mainloop()


if __name__ == "__main__":
    main()
