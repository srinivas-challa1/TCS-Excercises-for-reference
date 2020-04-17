

# Enter your code here. Read input from STDIN. Print output to STDOUT
class Employee:
    def __init__(self, name, id, age, gender):
        self.nm = name
        self.id = id
        self.age = age
        self.Gender = gender


class Organisation:
    def __init__(self, oname, elst):
        self.name = oname
        self.elist = elst

    def addEmployee(self, name, id, age, gender):
        e = Employee(name, id, age, gender)
        self.elist.append(e)

    def getEmployeeCount(self):
        return(len(self.elist))

    def findEmployeeAge(self, id):
        for i in range(len(self.elist)):
            if(self.elist[i].id == id):
                return(self.elist[i].age)
            elif(self.elist[i].id == id):
                continue
        else:
            return(-1)

    def countEmployees(self, age):
        older = 0
        for e in self.elist:
            if(e.age > age):
                older += 1
        return(older)


if __name__ == '__main__':
    employees = []
    o = Organisation('XYZ', employees)
    n = int(input())
    for i in range(n):
        name = input()
        id = int(input())
        age = int(input())
        gender = input()
        o.addEmployee(name, id, age, gender)

    id = int(input())
    age = int(input())
    print(o.getEmployeeCount())
    print(o.findEmployeeAge(id))
    print(o.countEmployees(age))
