class LeiFeng:

    def sweep(self):
        print("LeiFeng sweep")


class Student(LeiFeng):

    def sweep(self):
        print("Student sweep")


class Volunteer(LeiFeng):

    def sweep(self):
        print("Voluntter sweep")


class LeiFengFactory:

    def CreateLeiFeng(self):
        temp = LeiFeng()
        return temp


class StudentFactory(LeiFengFactory):

    def CreateLeiFeng(self):
        temp = Student()
        return temp


class VolunteerFactory(LeiFengFactory):

    def CreateLeiFeng(self):
        temp = Volunteer()
        return temp
