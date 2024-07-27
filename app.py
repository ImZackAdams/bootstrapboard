from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('suggestions.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS suggestions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            suggestion TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_suggestion', methods=['POST'])
def submit_suggestion():
    suggestion = request.form['suggestion']

    conn = sqlite3.connect('suggestions.db')
    c = conn.cursor()
    c.execute('INSERT INTO suggestions (suggestion) VALUES (?)',
              (suggestion,))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
