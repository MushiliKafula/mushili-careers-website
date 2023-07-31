from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Lusaka, Zambia',
  'salary': 'K45,000.00'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Ndola, Zambia',
  'salary': 'K40,000.00'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Kitwe, Zambia',
  'salary': 'K25,000.00'
}, {
  'id': 3,
  'title': 'Backend Engineer',
  'location': 'Livingstone, Zambia',
  'salary': 'K30,000.00'
}]


@app.route("/")
def welcome_page():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
