import sys
import dash
from dash.dependencies import Event, Output

import dash_core_components as dcc
import dash_html_components as dhtml

import plotly
import plotly.graph_objs as pgo

class DashVisualizer():
	def __init__(self, pi_data):
		self.app = dash.Dash(__name__)
		self.app.layout = dhtml.Div([
				dcc.Graph(id='live-pi-graph', animate=True),
				dcc.Interval(id='update-graph', interval=2000)
		])
		
		self.ix = 0
		self.pi_data = pi_data[2:] #Skip '3.'
		self.data_length = len(self.pi_data)
		self.x_axis = [str(label) for label in range(0, 9)]
		self.width = [.08 for width in range (0, 9)]
		self.y_axis = [0] * 10
		
		@self.app.callback(Output('live-pi-graph', 'figure'), 
							events=[Event('update-graph', 'interval')])
		def updateBarGraph():
			print(self.ix)
			if self.ix < self.data_length:
				self.y_axis[int(self.pi_data[self.ix])] +=1 # Count the number of occurences of a digit
				print(self.y_axis[int(self.pi_data[self.ix])])
				self.ix +=1
				data = pgo.Bar(x=self.x_axis, y=self.y_axis, width=self.width, visible=True, name="Digits of Pi")
				
				return {'data': [data], 'layout': pgo.Layout(xaxis=dict(range=[0, 9]), yaxis=dict(range=[0, max(self.y_axis)]))}
			else:
				sys.exit(0)