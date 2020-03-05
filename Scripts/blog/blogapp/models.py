from django.db import models
import csv



class Student(models.Model):
    clientID = models.CharField(max_length=20)
    Name = models.CharField(max_length=50)
    Father_Name = models.CharField(max_length=50)
    Mother_Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

    @classmethod
    def generatefromcsv(cls, file, keep_id=False):
        if isinstance(file, str):
            file = open(file, 'r')
        csvreader = csv.reader(file)
        schema_row = csvreader.__next__()
        for student in csvreader:
            data_dict = {schema_row[i]: student[i] for i in range(len(schema_row))}
            student_model = Student()
            for key, value in data_dict.items():

                if not keep_id and key == 'id':
                    continue
                setattr(student_model, key, value)
            import pdb
            pdb.set_trace()
            student_model.save()