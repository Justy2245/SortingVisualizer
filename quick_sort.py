def quick_sort(canvas, arr, draw_bar_chart, delay=100):
    def partition(low, high):
        # Choose the first element as the pivot
        pivot = arr[low]
        i = low + 1
        # Move all smaller elements to the left side
        for j in range(low + 1, high + 1):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                # Update the canvas
                draw_bar_chart(canvas, arr)
        # Swap the pivot element to its correct position
        arr[low], arr[i - 1] = arr[i - 1], arr[low]
        # Update the canvas
        draw_bar_chart(canvas, arr)
        return i - 1

    def quick_sort_step(low, high):
        if low < high:
            pi = partition(low, high)
            # Recursively sort elements before and after partition
            canvas.after(delay, quick_sort_step, low, pi - 1)
            canvas.after(delay, quick_sort_step, pi + 1, high)

    # Start sorting the entire array
    quick_sort_step(0, len(arr) - 1)