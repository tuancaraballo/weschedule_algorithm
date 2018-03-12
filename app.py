from flask import Flask
from flask import request
from flask import jsonify
from ast import literal_eval
from task_assignments import find_assignments
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


def tasksAlgorithm(tasks, people, shift):
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


@app.route('/tasks', methods=['GET', 'POST'])
def assignTasks():
    if request.method == 'POST':
        tasks = ''
        people = ''
        shift = ''
        # Fetches taks, people and shift from rquest
        try:
            tasks = json.loads(request.form['demand'])
            people = json.loads(request.form['people'])
            shift = tuple(json.loads(request.form['shift']))
            logging.debug('People --  %s', str(people))
            logging.debug('Tasks -- %s', str(tasks))
            logging.debug('Shift -- %s', str(shift))
        except Exception as e:
            logging.exception('Error fetching value from request: -- %s',str(e))
            raise
        # Run helper function that calls our algorithm
        x = tasksAlgorithm(tasks, people, shift)
        result = {}
        # Reformat result into a dictionary  {Person : [task1, task2]}
        for person in x.keys():
            person_tasks = []
            for demand in x[person]:
                person_tasks.append(demand.demand_name)
            result[person] = person_tasks
        logging.debug('Result -- %s', str(result))
        # Send response back
        return jsonify(result)
    else:
        logging.warning('Nothing to return')
        return 'nothing to return'

@app.route('/ma_task', methods=['GET', 'POST'])
def ma_task_handle():
    if request.method == 'POST':
        ma_info = ""
        task_info = ""
        result = ""
        try:
            data = request.get_json()
            ma_info = data.get('ma_info', {})
            task_info = data.get('task_info', {})

            logging.debug('Ma info --- %s', str(ma_info))
            logging.debug('Task info --- %s', str(task_info))

            # TODO: uncomment these three lines, when changes have been made
            result = find_assignments(ma_info, task_info)
            logging.debug('Result --- %s', str(result))
            return jsonify(result);

            # TODO: get rid of this return, use the one above after result returns

            # return "success from algorithm server"

        except Exception as e:
            logging.exception('Error fetching value from request: -- %s', str(e))
            return jsonify(str(e))
            raise
        return "post"
    else:
        return "got GET"
@app.route('/rooming_inbasket', methods=['GET', 'POST'])
def rooming_inbasket_handle():
    if request.method == 'POST':
        ma_info = ""
        doctor_info = ""
        rooming_result = ""
        inbasket_result = ""
        preferences = ""
        try:

            ma_info = request.form.getlist('ma_info')
            doctor_info = request.form.getlist('doctor_info')
            preferences = request.form.getlist('preferences')

            logging.debug('Ma info --- %s', str(ma_info))
            logging.debug('Task info --- %s', str(doctor_info))

            #algorithm will need ma_info, doctor_info and preferences
            #will return two schedules, the rooming and the inbasket schedule
            rooming_result, inbasket_result = find_assignments(ma_info, doctor_info, preferences)

            logging.debug('Result --- %s', str(rooming_result))
            logging.debug('Result --- %s', str(inbasket_result))

            result = {"rooming_result": rooming_result, "inbasket_result": inbasket_result}

            logging.debug('Result --- %s', str(result))
            return jsonify(result);
            # return "success from algorithm server"

        except Exception as e:
            logging.exception('Error fetching value from request: -- %s', str(e))
            return jsonify(str(e))
            raise
        return "post"
    else:
        return "got GET"

if __name__ == "__main__":
    app.run()


# ------- CODE THAT WE MAY USE LATER --------

# >>>>> Encoding for postman request of ma_info or task_info
            # ma_info = request.form["ma_info"]
            # ma_info = ma_info.encode('ascii','ignore')
            # ma_info = ma_info.decode("utf-8")
            # ma_info = literal_eval(ma_info)

            #ma_info = literal_eval(ma_info)

            # task_info = request.form["task_info"]
            # task_info = task_info.encode('ascii', 'ignore')
            # task_info = task_info.decode("utf-8")
            # task_info = literal_eval(task_info)

            #task_info = literal_eval(task_info)
