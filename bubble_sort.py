def bubble_sort(canvas, arr, draw_bar_chart, delay = 100):
    def sort_step(i, j):
        if i < len(arr):
            if j < len(arr) - i - 1:
                # Swap elements if needed
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Update the canvas
                draw_bar_chart(canvas, arr)
                # Schedule the next comparison
                canvas.after(delay, sort_step, i, j + 1)
            else:
                # Move to the next pass
                canvas.after(delay, sort_step, i + 1, 0)
        else:
            # Sorting is complete
            draw_bar_chart(canvas, arr)

    # Start the sorting process
    sort_step(0, 0)