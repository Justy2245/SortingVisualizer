def selection_sort(canvas, arr, draw_bar_chart, delay=100):
    def sort_step(i):
        if i < len(arr):
            min_index = i
            # Find the index of the minimum element
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            # Swap the minimum element with the first unsorted element
            arr[i], arr[min_index] = arr[min_index], arr[i]
            # Update the canvas
            draw_bar_chart(canvas, arr)
            # Schedule the next step
            canvas.after(delay, sort_step, i + 1)
        else:
            # Sorting is complete
            draw_bar_chart(canvas, arr)

    # Start the sorting process
    sort_step(0)
