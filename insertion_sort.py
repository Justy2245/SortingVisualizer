def insertion_sort(canvas, arr, draw_bar_chart, delay=100):
    def sort_step(i):
        if i < len(arr):
            j = i
            # Move the element to the correct position in the sorted portion
            while j > 0 and arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                j -= 1
                # Update the canvas
                draw_bar_chart(canvas, arr)
            # Schedule the next step
            canvas.after(delay, sort_step, i + 1)
        else:
            # Sorting is complete
            draw_bar_chart(canvas, arr)

    # Start from second element as first one is in sorted portion
    sort_step(1)
