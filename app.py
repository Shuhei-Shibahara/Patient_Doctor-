



class Doctor:
  def __init__(self, _name, _email):
    self.name = _name
    self.email = _email
    self.workout_list = {}
    self.patients = {}

  def add_patient(self, patient):
    self.patients[patient.id] = patient


class Patient:
  def __init__(self, _name, _email):
    self.name = _name
    self.email = _email
    self.workout_list = {}
    self.doctor = None


  