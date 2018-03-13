import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as dhtml

class DashVisualizer:
	def __init__(self):
		self.app = dash.Dash()
		# Layout has a div tag with 2 children, an <h1> and a React graph component
		self.app.layout = dhtml.Div(children=[
			dcc.Input(id='input', value='', type='text'),
			dhtml.Div(id='output')
			])
		
		@self.app.callback(Output(component_id='output', component_property='children'),
							[Input(component_id='input', component_property='value')])
		def updateValue(input_data):
			return "Input: {}".format(input_data)