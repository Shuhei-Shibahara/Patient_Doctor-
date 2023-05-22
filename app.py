

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
        self.exercise_list[doctor] = []

    def get_exercises(self):
        all_exercises = []
        for exercises in self.exercise_list.values():
            all_exercises.extend(exercises)
        return all_exercises


class Exercise:
    def __init__(self, name):
        self.name = name



  