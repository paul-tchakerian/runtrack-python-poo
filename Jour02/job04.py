class Student:
    def __init__(self, name, age, num_etudiant, credits):
        self._name = name
        self._age = age
        self._num_etudiant = num_etudiant  # 0 - 100
        self._credits = credits 

    def add_credits(self, credits):
        if credits > 0:
            self._credits += credits
            self._level = self._studentsEval()

    def _studentsEval(self):
        if self._credits >= 90:
            return "Excellent"
        elif self._credits >= 80:
            return "Très bien"
        elif self._credits >= 70:
            return "Bien"
        elif self._credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
        
    def studentInfo(self):
        return f"Nom: {self._name}, Age: {self._age}, Numéro d'étudiant: {self._num_etudiant}, Crédits: {self._credits}, Niveau: {self._level}"
    


student = Student("John", 36, 12, 124)
student.add_credits(10)
print(student._credits)
student.add_credits(-10)
print(student._credits)
student.add_credits(10)
print(student._credits)
student.add_credits(10)
print(student._credits)
print(student.studentInfo())