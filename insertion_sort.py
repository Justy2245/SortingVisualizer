def insertion_sort(canvas, arr, draw_bar_chart, delay=100):
    def sort_step(i):
        if i < len(arr):
            print(i)
            j = i
            while j > 0 and arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                j -= 1
                draw_bar_chart(canvas, arr)
            canvas.after(delay, sort_step, i + 1)
        else:
            draw_bar_chart(canvas, arr)
    sort_step(1)
