from flask import Flask, render_template, request, redirect, url_for
import random
import string

app = Flask(__name__)

participants = []

def generate_random_participant():
    participant = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    return participant

# Генерируем 10 случайных участников и добавляем их в список участников
random_participants = [generate_random_participant() for _ in range(10)]
participants.extend(random_participants)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/participants', methods=['GET', 'POST'])
def show_participants():
    if request.method == 'POST':
        name = request.form['name']
        if name not in participants:
            participants.append(name)
    return render_template('participants.html', participants=participants)

@app.route('/start_game')
def start_game():
    results = {}
    for participant in participants:
        results[participant] = random.randint(0, 100)
    winner = max(results, key=results.get)
    return render_template('results.html', results=results, winner=winner)

if __name__ == '__main__':
    app.run(debug=True)