from google.cloud import firestore
import logging

class FirebaseModel:
    def __init__(self):
        self.db = firestore.Client()  # El cliente Firestore usará automáticamente el proyecto especificado en las credenciales

    def get_all_visits(self):
        try:
            visits_ref = self.db.collection('visits')
            docs = visits_ref.stream()
            visits = []
            for doc in docs:
                visits.append(doc.to_dict())
            logging.info(f"Data obtained from Firestore: {visits}")
            return visits
        except Exception as e:
            logging.error(f"Error accessing data in collection 'visits': {e}")
            return None
