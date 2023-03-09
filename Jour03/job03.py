class Task:
    def __init__(self, title, description, status):
        self.title = title
    

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_tasks(self, task):   
        self.remove_tasks(task)

    def show_as_completed(self, task_number):
        self.task[task_number - 1].status = "Completed"

    def show_list(self):
        for task in self.tasks:
            print(f"_____\nTitre:\n {task.title}\Description: \n{task.description}\nStatus:\n {task.status})")

    def filter_list(self, filter):
        filtered_list = []
        for task in self.tasks_list :
            if task.status == filter:
                filtered_list.append(task)
        return filtered_list
    


tasks_list = TaskList()

TaskOne = Task("Tache 1", "Préparer dans un premier temps les pinceaux, les rouleau ainsi que le pot de peinture.", "En cours")
TaskTwo = Task("Tache 2","Acheter tout les ingrédients pour faire un bon repas pour les invités de demain soir", "A faire")
TaskThree = Task("Tache 3","Nettoyer la cuisine, la salle de bain et le salon.", "A faire")



print('---------------------   Taches 1  ---------------------')
tasks_list.add_task(TaskTwo)
tasks_list.add_task(TaskThree)


#print('---------------------   Taches 2 ---------------------')
#tasks_list.show_as_completed(TaskThree)


tasks_list.show_as_completed(2)

print(tasks_list.show_list(tasks_list.filter_list("A faire")))