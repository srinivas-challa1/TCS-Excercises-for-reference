class Employee:

    def __init__(self, emp_id, emp_name, emp_role, emp_salary):
        self.empId = emp_id
        self.empNm = emp_name
        self.empRole = emp_role
        self.empSal = emp_salary

    def increase_salary(self, percent):
        self.empSal += self.empSal*percent*0.01


class Organisation:
    def __init__(self, oname, emplst):
        self.org_name = oname
        self.emp_list = emplst

    def calculate_increment(self, role, percent):
        incemp = []
        for emp in self.emp_list:
            if(emp.empRole == role):
                emp.increase_salary(percent)
                incemp.append(emp)
        return(incemp)


if __name__ == "__main__":
    emplst = []
    count = int(input())
    for i in range(count):
        eid = int(input())
        ename = input()
        erole = input()
        esal = int(input())
        emplst.append(Employee(eid, ename, erole, esal))
    o = Organisation("XYZ", emplst)
    inprole = input()
    inp_percent = int(input())
    result = o.calculate_increment(inprole, inp_percent)
    if(len(result) != 0):
        for emp in result:
            print(emp.empNm, '\t', emp.empSal)
    else:
        print("No Employee found with the given role!")
