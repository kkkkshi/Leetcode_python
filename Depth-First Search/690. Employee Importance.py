# 690. Employee Importance

class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


# breadth-first Approach
# Time: O(n)
# Space: O(n)
# 2023.07.01: yes
# notes: map id to employee, recurse from the queried id and sum the
#        importance of the employee and all subordinates
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        def recursion(employees, id):
            employee = emap[id]
            self.total_points += employee.importance
            if employee.subordinates:
                for id in employee.subordinates:
                    recursion(employees, id)
        self.total_points = 0
        emap = {e.id: e for e in employees}
        recursion(employees, id)
        return self.total_points


# notes: same idea, return the sum directly from the recursion
class Solution2:
    def getImportance(self, employees, query_id):
        """
        :type employees: List[Employee]
        :type query_id: int
        :rtype: int
        """
        emap = {e.id: e for e in employees}
        def dfs(eid):
            employee = emap[eid]
            return (employee.importance +
                    sum(dfs(eid) for eid in employee.subordinates))
        return dfs(query_id)


# Tests:
for sol in (Solution(), Solution2()):
    e1 = [Employee(2, 3, []), Employee(3, 3, []), Employee(1, 5, [2, 3])]
    e2 = [Employee(1, 2, [5]), Employee(5, -3, [])]
    assert sol.getImportance(e1, 1) == 11
    assert sol.getImportance(e1, 2) == 3
    assert sol.getImportance(e2, 1) == -1
    assert sol.getImportance(e2, 5) == -3
