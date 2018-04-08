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


