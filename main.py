import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from bubble_s import bubble_sort
from heap_s import heap_sort
from shell_s import shell_sort
from insertion_s import insertion_sort
from selection_s import selection_sort

n_elements = int(input('Enter number of elements: '))
alg_choice = int(input('Choose algorithm: \n 1. Bubble Sort '
            '\n 2. Heapify Sort \n 3. Shell Sort \n 4. Insertion Sort'
            '\n 5. Selection Sort \n'))

array = [i + 1 for i in range(n_elements)]
random.shuffle(array)

if(alg_choice == 1):
    title = 'Bubble Sort'
    algo = bubble_sort(array)
elif(alg_choice == 2):
    title = 'Heapify Sort'
    algo = heap_sort(array)
elif(alg_choice == 3):
    title = 'Shell Sort'
    algo = shell_sort(array)
elif(alg_choice == 4):
    title = 'Insertion Sort'
    algo = insertion_sort(array)
elif(alg_choice == 5):
    title = 'Selection Sort'
    algo = selection_sort(array)


fig, ax = plt.subplots()
ax.set_title(title)


bar_rec = ax.bar(range(len(array)), array, align='edge')

ax.set_xlim(0, n_elements)
ax.set_ylim(0, int(n_elements * 1.1))

text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

epochs = [0]


def update_plot(array, rec, epochs):
    for rec, val in zip(rec, array):
        rec.set_height(val)
    epochs[0] += 1
    text.set_text("No.of operations :{}".format(epochs[0]))


anima = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rec, epochs), frames=algo, interval=1, repeat=False)
plt.show()
