



class Doctor:
  def __init__(self, _name, _email):
    self.name = _name
    self.email = _email
    self.workout_list = []
    self.patients = []

  def add_patient(self, patient):
    self.patients[patient.id] = patient
  
  def add_exercise(self, exercise):

        self.patients[patient.id] = patient

class Patient:
  def __init__(self, _name, _email):
    self.name = _name
    self.email = _email
    self.workout_list = {}
    self.doctor = None

class Exercise:
  def __init__(self) -> None:
    pass


  