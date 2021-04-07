import pickle


def assess_subjectivity(text):
    arr = ObjectivityAssessor.model_direct.predict_proba(text)
    return arr[0][1] * 100


def assess_objectivity(text):
    arr = ObjectivityAssessor.model_direct.predict_proba(text)
    return arr[0][1] * 100


class ObjectivityAssessor:
    model_direct = pickle.load(open('objectivity-detection-direct.sav', 'rb'))
