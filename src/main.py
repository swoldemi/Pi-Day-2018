from DashDataVisualization import DashVisualizer
# Quantum entropy Visualization w/ Dash by @swoldemi (maybe)

def main():
	dasher = DashVisualizer()
	dasher.app.run_server(debug=True)

if __name__ == '__main__':
	main()