import sys
import dash
from dash.dependencies import Event, Output

import dash_core_components as dcc
import dash_html_components as dhtml

import plotly
import plotly.graph_objs as pgo

from collections import deque

class DashVisualizer():
	def __init__(self, pi_data):
		self.app = dash.Dash(__name__)
		self.app.layout = dhtml.Div([
				dcc.Graph(id='live-pi-graph', animate=True),
				dcc.Interval(id='update-graph', interval=300),
				dhtml.Output(id='pi-output')])
		self.ix = 0
		self.pi_string = ''
		self.pi_data = pi_data[2:] #Skip '3.'
		self.data_length = len(self.pi_data)
		self.y_axis = deque(maxlen=150)
		self.x_axis = deque(maxlen=150)
		
		@self.app.callback(Output('live-pi-graph', 'figure'), 
							events=[Event('update-graph', 'interval')])
		def updateBarGraph():
			if self.ix < self.data_length:
				self.x_axis.append(self.ix)
				self.y_axis.append(self.pi_data[self.ix])
				self.ix +=1
				data = pgo.Scatter(x=list(self.x_axis), y=list(self.y_axis), name="Digits of Pi",
				mode = 'lines+markers', marker=dict(size=10, color='rgba(255, 0, 0, .9)', line=dict(width=2)))
				return {'data': [data], 'layout': pgo.Layout(title='Pi Day 2018 by @swoldemi', xaxis=dict(range=[min(self.x_axis), max(self.x_axis)]), yaxis=dict(range=[0, 12]), autosize=True)}
			else:
				sys.exit(0)
		@self.app.callback(Output(component_id='pi-output', component_property='children'), 
		events=[Event('update-graph', 'interval')])
		def printPi():
			if self.ix-1 < self.data_length:
				self.pi_string = self.pi_string + self.pi_data[self.ix-1]
				return self.pi_string
			