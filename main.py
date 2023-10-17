class Task:
    def __init__(self, name_in_constructor, description):
        self.name = name_in_constructor
        self.description = description
        self.is_done = False

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
            input_task_name = input('enter your task name \n')
            input_task_description = input('enter your task description \n')
            tasks.append(Task(input_task_name, input_task_description))
        elif choice == '2':
            for i in range(len(tasks)):
                print(f'{i}) {tasks[i].name} - {tasks[i].description}, {"done" if tasks[i].is_done else "in progress"}')
        elif choice == '3':
            task_number = input('enter your task number\n')
            tasks[int(task_number)].is_done = True
        elif choice == '4':
            task_number = input('enter your task number\n')
            tasks.remove(tasks[int(task_number)])
        elif choice == '5':
            return
        else:
            print('wrong value')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    to_do_cli()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
