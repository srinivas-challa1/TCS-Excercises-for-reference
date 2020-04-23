class Employee:
    def __init__(self, num, name, leaves):
        self.empno = num
        self.empname = name
        self.Leaves = leaves


class Company:
    def __init__(self, cmpname, emplst):
        self.cname = cmpname
        self.emps = emplst

    def display_leave(self, eno, leaveType):
        for emp in self.emps:
            if(emp.empno == eno):
                return(emp.Leaves[leaveType])

    def leave_application(self, empno, leaveType, nol):
        check = False
        for emp in self.emps:
            if(emp.empno == empno):
                for (lt, lb) in emp.Leaves.items():
                    if(lt == leaveType and lb >= nol):
                        check = True
        if (check):
            return("Granted")
        else:
            return("Rejected")


if __name__ == "__main__":
    n = int(input())
    emps = []
    c = Company('ABC', emps)
    for i in range(n):
        leaves = {}
        eno = int(input())
        ename = input()
        leaves['CL'] = int(input())
        leaves['EL'] = int(input())
        leaves['SL'] = int(input())
        e = Employee(eno, ename, leaves)
        c.emps.append(e)
    empno = int(input())
    ltype = input()
    nol = int(input())
    print(c.display_leave(empno, ltype))
    print(c.leave_application(empno, ltype, nol))
