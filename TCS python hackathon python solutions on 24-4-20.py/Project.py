

class Project:
    def __init__(self, pid, pname, ct, tlst):
        self.projectId = pid
        self.projectName = pname
        self.manHours = ct
        self.technologyList = tlst
        self.avgProjCost = 0

    def calculateProjCost(self, ratePerManHour):
        return(self.manHours*ratePerManHour)


class Organization:
    def __init__(self, oname, plist):
        self.organizationName = oname
        self.projList = plist

    def projAvgCostByTechnology(self, Pid, ratePerManHour):
        for proj in self.projList:
            if(proj.projectId == Pid):
                proj.avgProjCost = (proj.calculateProjCost(ratePerManHour)/len(proj.technologyList))
                return(proj)
        else:
            return(None)


if __name__ == "__main__":
    projectList = []
    count = int(input())
    for _ in range(count):
        projectId = int(input())
        projectName = input()
        manHours = int(input())
        tc = int(input())
        technologyList = []
        for _ in range(tc):
            technologyList.append(input())
        P = Project(projectId, projectName, manHours, technologyList)
        projectList.append(P)
    org = Organization("ABC", projectList)
    projId = int(input())
    rate = int(input())
    avgProj = org.projAvgCostByTechnology(projId, rate)
    if(avgProj == None):
        print("No Project Exists")
    else:
        print(avgProj.projectId, avgProj.projectName, avgProj.manHours,
              avgProj.technologyList, avgProj.avgProjCost)
