# -*- coding: cp1252 -*-

from flask import jsonify, request, Flask, render_template
app = Flask(__name__)

@app.route('/services')
def service():
   return render_template('services.html')

@app.route('/PieChart')
def PieChart():
   return render_template('PieChart.html')

@app.route('/')
def PieChart2():
   return render_template('PieChart2.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))

@app.route('/pie-chart')
def google_pie_chart():
	data = {'Task' : 'Hours per Day', 'Work' : 11, 'Eat' : 2, 'Commute' : 2, 'Watching TV' : 2, 'Sleeping' : 7}
	#print(data)
	return render_template('pie-chart.html', data=data)



if __name__ == '__main__':
   app.run(debug = True)
