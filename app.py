from flask import Flask
from flask import request
import logging
import json

from test import *

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


@app.route('/')
def index():
    return 'Hello Tuan'


@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


def helper(tasks, people, shift):

    list_demands = []
    for task in tasks:
        list_demands.append(daily_demand(task))
    demand_schedule = demand_daily_resource(list_demands)

    people_shifts_dic = {}
    for person in people:
        people_shifts_dic[person] = shift

    MA_master_schedule = daily_master_schedule(people_shifts_dic)
    solver = assign(demand_schedule, MA_master_schedule, "divide_equally")
    x = solver.solve()

    return x

    # demand_names_list = ["clean rooms", "replace fax paper", "replace printer paper", "send billing paperwork", "clean emails"]
    # list_demands = []
    #
    # for task in demand_names_list:
    #     list_demands.append(daily_demand(task))
    #
    # demand_schedule = demand_daily_resource(list_demands)
    # people = ["Maria Chavez", "Sally Puentes", "Gustavo Chavez"]
    # shift = ("900","1700")
    #
    # people_shifts_dic = {}
    # for person in people:
    #     people_shifts_dic[person] = shift
    #
    # MA_master_schedule = daily_master_schedule(people_shifts_dic)
    # solver = assign(demand_schedule, MA_master_schedule, "divide_equally")
    # x = solver.solve()
    #
    # return x

@app.route('/test', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        tasks = ''
        people = ''
        shift = ''
        try:
            tasks = json.loads(request.form['demand'])
            people = json.loads(request.form['people'])
            shift = tuple(json.loads(request.form['shift']))
        except e:
            raise e
        logging.debug('People --  %s', str(people))
        logging.debug('Tasks -- %s', str(tasks))
        logging.debug('Shift -- %s', str(shift))

        x = helper(tasks, people, shift)

        logging.debug('x -- %s', str(x));
        result = {}
        for person in x.keys():
            person_tasks = []
            for demand in x[person]:
                person_tasks.append(demand.demand_name)
            result[person] = person_tasks
        print('RESULT', result)
        logging.warning('Result -- %s', str(result))

        try:
            result = json.dumps(result)
        except:
            print('Error dumping')
            logging.debug('Error dumping')

        return result
    else:
        logging.warning('Nothing to return')
        return 'nothing to return'


if __name__ == "__main__":
    app.run()
