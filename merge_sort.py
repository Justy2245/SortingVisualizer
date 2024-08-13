def merge_sort(canvas, arr, draw_bar_chart, delay=100):
    def merge(low, mid, high, callback):
        # Create temporary arrays to hold the two halves
        left = arr[low:mid + 1]
        right = arr[mid + 1:high + 1]

        i = 0  # Index for the left half
        j = 0  # Index for the right half
        k = low  # Index for the merged array

        def merge_step():
            nonlocal i, j, k
            if i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
                draw_bar_chart(canvas, arr)
                canvas.after(delay, merge_step)
            else:
                # Copy any remaining elements of left half
                while i < len(left):
                    arr[k] = left[i]
                    i += 1
                    k += 1
                    draw_bar_chart(canvas, arr)
                    canvas.after(delay, merge_step)
                    return
                # Copy any remaining elements of right half
                while j < len(right):
                    arr[k] = right[j]
                    j += 1
                    k += 1
                    draw_bar_chart(canvas, arr)
                    canvas.after(delay, merge_step)
                    return
                # After merge completes
                callback()

        merge_step()

    def merge_sort_step(low, high, callback):
        if low < high:
            mid = (low + high) // 2
            def after_sorting():
                merge(low, mid, high, callback)

            # Recursively sort the first and second halves
            merge_sort_step(low, mid, lambda: merge_sort_step(mid + 1, high, after_sorting))

        else:
            callback()

    # Start sorting the entire array
    merge_sort_step(0, len(arr) - 1, lambda: draw_bar_chart(canvas, arr))
