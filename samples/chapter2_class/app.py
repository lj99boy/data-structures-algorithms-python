import datetime

class PersonTypeError(TypeError):
    pass

class PersonValueError(ValueError):
    pass

class Person:
    _num = 0

    def __init__(self,name,sex,birthday,ident):
        if not (isinstance(name,str) and sex in ("female","male")):
            raise PersonValueError(name,sex)

        try:
            birth = datetime.date(*birthday)
        except:
            raise PersonValueError("Wrong date:",birthday)

        self._name = name
        self._sex = sex
        self._birthday = birth
        self._id = ident
        Person._num += 1

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if not isinstance(name,str):
            raise PersonValueError("set_name",name)
        self._name = name

    @property
    def sex(self):
        return self._sex

    @property
    def birthday(self):
        return self._birthday

    @property
    def age(self):
        return (datetime.date.today().year - self._birthday.year)

    def __lt__(self, other):
        if not isinstance(other,Person):
            raise PersonTypeError(other)
        return self._id < other._id

    @classmethod
    def num(cls):
        return cls._num

    def __str__(self):
        return " ".join((self._id,self._name,self._sex,str(self._birthday)))

    def details(self):
        return ", ".join(
            (
                'code: '+ self._id,
                'name: '+self._name,
                'gender: '+self._sex,
                'birthday: '+str(self._birthday)
            )
        )



class Student(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls):
        cls._id_num += 1
        year = datetime.date.today().year
        return "1{:04}{:05}".format(year,cls._id_num)

    def __init__(self,name,sex,birthday,department):
        super().__init__(
            name,
            sex,
            birthday,
            Student._id_gen()
        )
        self._department = department
        self._enroll_date = datetime.date.today()
        self._courses = {}

    @property
    def scores(self):
        return [(cname,self._courses[cname]) for cname in self._courses]

    def set_score(self,course_name,score):
        if course_name not in self._courses:
            raise PersonValueError("No this course selected:",course_name)

        self._courses[course_name] = score

    def set_course(self,course_name):
        self._courses[course_name] = None

    def details(self):
        return ", ".join((super().details(),
                         'enroll_date: '+str(self._enroll_date),
                         'department: '+self._department,
                         'courses: '+ str(self.scores)
                         ))

# s1 = Student('s1','female',(1990,10,1),'miao')
# print(s1)
# print(s1.details())


class Staff(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls,birthday):
        cls._id_num +=1
        birth_year = datetime.date(*birthday).year
        return "0{:04}{:05}".format(birth_year,cls._id_num)

    def __init__(self,name,sex,birthday,entry_date=None):
        super().__init__(name,sex,birthday,self._id_gen(birthday))

        if entry_date:
            try:
                self._entry_date = datetime.date(*entry_date)
            except:
                raise PersonValueError("Wrong date:",entry_date)
        else:
            self._entry_date = datetime.date.today()

        self._salary = 1720
        self._department = "unknown"
        self._position = "unknown"

    def set_salary(self,amount):
        if not type(amount) is int:
            raise TypeError
        self._salary = amount

    def set_position(self,position):
        self._position = position

    def set_department(self,department):
        self._department = department

    def details(self):
        return ", ".join((super().details(),
                         'entry_date: '+str(self._entry_date),
                         'department: '+self._department,
                         'position: '+ str(self._position),
                         'salary: '+ str(self._salary),
                         ))

