from DashDataVisualization import DashVisualizer
# Visualizing the first billion digits of Pi using Dash (for Pi Day 2018!)

def getData():
	with open('../billion-pi-digits.txt', 'rt') as pi_digits:
		digits = list(str(pi_digits.readlines()).replace('[', '').replace(']','').strip("'"))
		pi_digits.close()
	return digits


if __name__ == '__main__':
	dasher = DashVisualizer(getData())
	server = dasher.app.server
	app = dasher.app
	app.run_server(debug=True)