

class Doctor:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def assign_exercises(self, patient, exercises):
        patient.assign_exercises(self, exercises)


class Patient:
    def __init__(self, name):
        self.name = name
        self.exercise_list = {}

    def assign_exercises(self, doctor, exercises):
      if self.exercise_list[doctor]:
        self.exercise_list[doctor].append(exercises)
      else:
        self.exercise_list[doctor] = [exercises]

    def get_exercises(self):
        
        return self.exercise_list


class Exercise:
    def __init__(self, name):
        self.name = name



  