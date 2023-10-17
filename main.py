# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def print_mult_table():
    for i in range(9):
        for j in range(9):
            sumr = (i+1)*(j+1)
            print(f'{i+1} * {j+1} = {sumr}')
        print()

# create a list of tasks, add task, count tasks, add as resolved, delete task
# create an empty task massive; show names of tasks with prints, accept task from the user, switch construction -

def to_do_cli():
    tasks = []
    print('my to do cli app')
    print('1) add task')
    print('2) view tasks')
    print('3) mark task as done')
    print('4) delete task')
    print('5) exit task')
    while True:

        choice = input('enter your choice \n')


        if choice == '1':
            task = input('enter your task\n')
            tasks.append([task, False])
        elif choice == '2':
            for task in tasks:
                print(f'{task[0]} - {task[1]}')
        elif choice == '3':
            task_number = input('enter your task number\n')
            tasks[int(task_number)-1][1] = True
        elif choice == '4':
            task_number = input('enter your task number\n')
            tasks.remove(tasks[int(task_number)-1])
        elif choice == '5':
            return
        else:
            print('wrong value')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    to_do_cli()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
