import tkinter as tk

globalData = [25, 50, 75, 100, 50, 75, 100, 10, 21, 1, 2, 3, 0]
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
def draw_bar_chart(canvas, data, width=600, height=400):
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

def update(event, canvas, entry):
    string = entry.get()

    if(string.endswith(',') == False):
        # Split the string by commas
        string_list = string.split(',')
        global globalData
        globalData = list(map(int, string_list))
        draw_bar_chart(canvas, globalData)

def main():
    root = tk.Tk()
    root.title("Bar Chart")

    entry = tk.Entry(root)
    entry.grid(row=0,column=0)
    # Create a Canvas widget
    canvas = tk.Canvas(root, width=600, height=400, bg="white")
    canvas.grid(row=1,column=0)

    button = tk.Button(root, text="Sort", command=lambda: bubble_sort(canvas, globalData))
    button.grid(row=2,column=0)

    root.bind("<KeyPress>", lambda event: update(event, canvas, entry))

    root.mainloop()


if __name__ == "__main__":
    main()
