#TO-DO-LIST
tasks = []

while True : 
    print("-----TO - DO - LIST------")
    print("1.Add Tasks")
    print("2.Show Tasks")
    print("3.Exit")

    choice = int(input("what do you want to do today !"))

    if choice ==1 : 
        add_task = input("Enter the task : ")
        new_task = {
            "id" : len(tasks) + 1,
            "add_task" : add_task,
            "status" : "pending"
        }
        tasks.append(new_task)
        print("task added successfully")

    elif choice == 2 :
        if len(tasks) == 0 :
            print("No task available")
        else :
            print("\n ----- your work----")
            for i , kaam in enumerate(tasks,1):
                print(f"{kaam['id']}. {kaam['add_task']}")
    elif choice == 3 :
        print("sayonara")
        break
    else :
        print("please enter a valid input!!!")