class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class User:
    def __init__(self, userID):
        self.userID = userID

class Survey:
    def __init__(self, surveyID, survey_name, course):
        self.surveyID = surveyID
        self.survey_name = survey_name
        self.course = course
//for tesing purposes
