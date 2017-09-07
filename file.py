import csv

def create_survey(new_survey, survey_name):
   with open(str(survey_name) + '.csv','w') as csv_make:
      writer = csv.writer(csv_make)
      writer.writerow(new_survey)

def read(csv_file):
   items = []
   with open(csv_file,'r') as csv_in:
      reader = csv.reader(csv_in)
      for row in reader:
         items.append(row)
   return items
