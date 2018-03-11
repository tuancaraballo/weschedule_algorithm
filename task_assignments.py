from ortools.linear_solver import pywraplp
from numpy import zeros
'''
This python file will contain the functions to handle the task assignment.

INPUT
ma_info:
task_info:

'''

# TODO: fix now algorithm handles names ie it gets names from variable name line 90
# TODO: fix dates currently using just an int
# TODO: handle specific times ie what if task needs to be done at 9am on 15th day? Must be done by employee who is working there
# TODO: should error sanity checking be done here or at ui? (ui most likely, but we havent decided)
#

def find_assignments(ma_info, task_info):

    # make matrix to store all the variables, will be num_ma x num_task_days
    num_cols = 0
    for row in range(len(task_info)):
        num_cols = num_cols + len(task_info[row]["due_dates"])

    expanded_tasks = []
    for idx, task in enumerate(task_info):
        for day in task["due_dates"]:
            expanded_tasks = expanded_tasks + [(task["key"], task["skills_req"], task["effort"], day)]
    # print(len(expanded_tasks))

    matrix_vars = zeros((len(ma_info), len(expanded_tasks)), dtype=object)
    # print("matrix_vars is of shape {}".format(matrix_vars.shape))

    solver = pywraplp.Solver('SolveIntegerProblem',
                             pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    # make all the variables

    # make a list of tuples (task_name, skill, weight, day_due)
    #notice that day_due is a int not a list of ints

    expanded_tasks = []
    for idx, task in enumerate(task_info):
        for day in task["due_dates"]:
            expanded_tasks = expanded_tasks + [(task["key"], task["skills_req"], task["effort"], day)]
    #print(expanded_tasks)

    for row, single_ma_info in enumerate(ma_info):
        # print(single_ma_info)
        for col, single_task_info in enumerate(expanded_tasks):
            # check if ma is working on day due
            # check if ma has skills
            print(single_task_info)
            if single_task_info[3] in single_ma_info["availability"] and single_task_info[1] == 'none' or single_task_info[1] in single_ma_info["skills"]:
                var_name = single_ma_info["key"] + " " + single_task_info[0] + " " + str(single_task_info[3])
                print(var_name)
                matrix_vars[row, col] = solver.IntVar(0.0, 1.0, var_name)
            else:
                matrix_vars[row, col] = "none"

    # make all the cosntraints
#
    # print("shape of matrix is {}".format(matrix_vars.shape))
    # print("len of expaneded is {}".format(len(expanded_tasks)))

    z = solver.IntVar(0.0, solver.infinity(), "z")
    ma_constraints = []
    for row in range(matrix_vars.shape[0]):
        constraint = solver.Constraint(-solver.infinity(), 0)
        constraint.SetCoefficient(z, -1)
        for col in range(matrix_vars.shape[1]):
            if type(matrix_vars[row, col]) != type("none"):
                constraint.SetCoefficient(matrix_vars[row, col], expanded_tasks[col][2])
        ma_constraints = ma_constraints + [constraint]

    task_constraints = []
    for col in range(matrix_vars.shape[1]):
        constraint = solver.Constraint(1, 1)
        for row in range(matrix_vars.shape[0]):
            if type(matrix_vars[row, col]) != type("none"):
                constraint.SetCoefficient(matrix_vars[row, col], 1)
        task_constraints = task_constraints + [constraint]



    #run optimizer
    objective = solver.Objective()
    objective.SetCoefficient(z, 1)
    objective.SetMinimization()
    result_status = solver.Solve()

    # reconstruct

    result = {}
    for row in range(matrix_vars.shape[0]):
        for col in range(matrix_vars.shape[1]):
            if type(matrix_vars[row, col]) != type("none") and matrix_vars[row, col].solution_value() == 1:
                var_name = matrix_vars[row, col].name().split()
                ma_name = var_name[0]
                day = int(var_name[-1])
                task_name = " ".join(var_name[1: -1])
                task = {}
                task['task_key'] = task_name
                task['due_date'] = day
                if ma_name not in result.keys():
                    result[ma_name] = [task]
                else:

                    result[ma_name] = result[ma_name] + [task]
    #create dictionary that maps ma_name to typle with (assignment name, date_due)
    # print(result)
    return result

    #return answer
