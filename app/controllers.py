from .models import FirebaseModel

class DataController:
    def __init__(self):
        self.model = FirebaseModel()

    def get_all_visits(self):
        return self.model.get_all_visits()
