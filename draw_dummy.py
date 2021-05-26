import plotly.graph_objects as go
animals=['giraffes', 'orangutans', 'monkeys',"abc","efg"]


y1=[0.001158395575, 0.5408099144, 0.0529625351, 1.151367188, 1.333333333]
y2 = [0.001639344262, 0.5368298368, 0.06140724947, 1.153316547, 1.338295388]
y3 = [0.001183395575, 0.5407870133, 0.05296247554, 1.151367188, 1.333333254]

y1= [0.1, 0.54, 0.05, 1.15, 1.33]
y1= [0.1, 0.2, 0.3, 0.4, 0.5]
y2 = [0.1, 0.53, 0.06, 1.15, 1.338]
y2= [0.1, 0.2, 0.3, 0.4, 0.5]
y3 = [0.1, 0.54, 0.05, 1.15, 1.33]
y3= [0.1, 0.2, 0.3, 0.4, 0.5]
print(type(y1[0]))
# Change the bar mode
fig = go.Figure(data=[
    go.Bar(name='SF Zoo', x=animals, y=y1),
    go.Bar(name='LA Zoo', x=animals, y=y2),
    # go.Bar(name='LM Zoo', x=animals, y=y3)
])
fig.update_layout(barmode='stack')
# fig.show()


import plotly.graph_objects as go
animals=['giraffes', 'orangutans', 'monkeys']

fig = go.Figure(data=[
    go.Bar(name='SF Zoo', x=animals, y=[2, 5, 2]),
    go.Bar(name='LA Zoo', x=animals, y=[1, 1, 2])
])
# Change the bar mode
fig.update_layout(barmode='relative')
fig.show()