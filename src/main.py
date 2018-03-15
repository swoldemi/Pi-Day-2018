from DashDataVisualization import DashVisualizer
# Visualizing the first billion digits of Pi using Dash (for Pi Day 2018!)

def main():
	with open('../billion-pi-digits.txt', 'rt') as pi_digits:
		digits = list(str(pi_digits.readlines()).replace('[', '').replace(']','').strip("'"))
		pi_digits.close()

	dasher = DashVisualizer(digits)
	dasher.app.run_server(debug=True)
	return dasher.app.server
	
if __name__ == '__main__':
	server = main()