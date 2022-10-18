from flask import Blueprint, render_template, request, session
import random
from data_stuff.distribution_factory import normal, normal1, normal2, normal3


play = Blueprint('play', __name__)

DISTRIBUTIONS = {
#   'name': distribution_function
    'Normal': normal,
    'Normal1': normal1,
    'Normal2': normal2,
    'Normal3': normal3,
}


def get_random_distribution():
    name, distribution_function = random.choice(list(DISTRIBUTIONS.items()))
    return distribution_function(100), name # Change to n instead of 100

def get_random_options(correct_option):
    distribution_names = list(DISTRIBUTIONS.keys())
    distribution_names.remove(correct_option)
    wrong_options = random.sample(distribution_names, 3)
    return [correct_option] + wrong_options

@play.route('/play', methods=['GET'])
@play.route('/', methods=['GET'])
def question():
    distribution, correct_option = get_random_distribution()
    session['correct_option'] = correct_option
    answer_options = get_random_options(correct_option)
    return render_template('play.html', distribution=distribution, answer_options=answer_options)

@play.route('/api/check_answer', methods=['POST'])
def api_answer():
    selected_option = request.form.get('selected_option')
    correct_option = session.get('correct_option')
    print(selected_option, correct_option)
    # Check if the answer is correct
    return str(selected_option == correct_option)