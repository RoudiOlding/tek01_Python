
def addTask(ftask):
    notionTask['name'].append(ftask)
    notionTask['status'].append('pending')

def viewTask(fNotionTask):

    if not fNotionTask['name']:
        print("There's no task!!")

    for i in range(len(fNotionTask['name'])):
        print(f"Task {i}. {fNotionTask['name'][i]} -- {fNotionTask['status'][i]}\n")

def markTask(fNotionTask):
    listOptions = []
    print("Select the task you want to mark as completed:\n")

    for i in range(len(fNotionTask['name'])):
        if fNotionTask['status'][i] == 'pending':
            print(f"{i}. {fNotionTask['name'][i]} -- {fNotionTask['status'][i]}")
            listOptions.append(i)

    if not listOptions:
        print("Not pending tasks found!")
        return

    while True:
        try:
            option = int(input('Choose one: '))
            if option in listOptions:  # Check if the option is valid
                fNotionTask['status'][option] = 'completed'
                print(f"Task '{fNotionTask['name'][option]}' marked as completed!")
                break
            else:
                print("Invalid option. Please choose a valid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def deleteTask(fTask):
    print("Select the task you want to delete:\n")
    listOptions = []

    for i in range(len(fTask['name'])):
        print(f"{i}. {fTask['name'][i]} -- {fTask['status'][i]}")
        listOptions.append(i)

    if not fTask:
        print("No tasks found!")
        return
    
    while True:
        try:
            option = int(input('Choose one: '))
            if option in listOptions:  # Check if the option is valid
                fTask['name'].pop(option)
                fTask['status'].pop(option)
                print(f"Task {option}... deletect succesully!")
                break
            else:
                print("Invalid option. Please choose a valid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    print("Welcome to exercise 7")

    notionTask = {
        'name': [],
        'status': [] # completed, pending
    }

    option = 0
    while option != 5:
        option = int(input('Choose an option: \n' + '1. Add tasks\n' + '2. Mark tasks as completed\n' +
                        '3. Delete tasks\n' + '4. View pending and completed tasks\n' + '5. Exit\n'))
        if option==1:
            task = input('Insert the task: ')
            addTask(task)
        elif option==2:
            markTask(notionTask)
        elif option==3:
            deleteTask(notionTask)
        elif option==4:
            viewTask(notionTask)
        elif option==5:
            print('Goodbye')
            option = 5
        else:
            print('Invalid option, try again!\n')
