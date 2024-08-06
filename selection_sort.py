def selection_sort(canvas, arr, draw_bar_chart, delay = 100):
    def sort_step(i):
        if(i < len(arr)):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
            draw_bar_chart(canvas, arr)
            canvas.after(delay, sort_step, i + 1)
        else:
            draw_bar_chart(canvas, arr)
    sort_step(0)
