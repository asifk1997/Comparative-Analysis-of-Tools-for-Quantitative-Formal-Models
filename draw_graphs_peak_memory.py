# import plotly.graph_objects as go
#
# data_point = ['cluster.v1.jani', 'embedded.v1.jani', 'fms.v1.jani', 'kanban.v1.jani', 'polling.12.v1.jani']
# y1 = [57, 57, 50, 50, 58]
# y1_text = [57, 57, "INCOMPATIBLE", "INCOMPATIBLE", 58]
# y2 = [68, 57, 54, 56, 87]
# y3 = [122, 123, 122, 125, 193]
# fig = go.Figure(data=[
#     go.Bar(name='MODES', x=data_point, y=y1_text, text=y1_text, textposition='auto', showlegend=True),
#     go.Bar(name='MCSTA', x=data_point, y=y2, text=y2, textposition='auto', showlegend=True),
#     go.Bar(name='STORM', x=data_point, y=y3, text=y3, textposition='auto', showlegend=True),
#
# ])
# # Change the bar mode
# fig.update_layout(barmode='group')
# fig.update_layout(title="CTMC Peak memory usage comparison")
# fig.update_layout(xaxis_title="CTMC Models")
# fig.update_layout(yaxis_title="peak memory usage")
# fig.write_image("fig1.png")

# import plotly.graph_objects as go
#
# data_point = ['brp.v1.jani', 'crowds.v1.jani', 'egl.v1.jani', 'herman.3.v1.jani', 'leader_sync.3-2.v1.jani']
# y1 = [57, 57, 59, "INCOMPATIBLE", 57]
# y1_text = [57, 57, "INCOMPATIBLE", "INCOMPATIBLE", 58]
# y2 = [52, 54, 62, "INCOMPATIBLE", 53]
# y3 = [122, 122, 130, 109, 122]
# fig = go.Figure(data=[
#     go.Bar(name='MODES', x=data_point, y=y1, text=y1, textposition='auto', showlegend=True),
#     go.Bar(name='MCSTA', x=data_point, y=y2, text=y2, textposition='auto', showlegend=True),
#     go.Bar(name='STORM', x=data_point, y=y3, text=y3, textposition='auto', showlegend=True),
#
# ])
# # Change the bar mode
# fig.update_layout(barmode='group')
# fig.update_layout(title="DTMC Peak memory usage comparison")
# fig.update_layout(xaxis_title="DTMC Models")
# fig.update_layout(yaxis_title="peak memory usage")
# fig.write_image("fig1DTMC.png")


# import plotly.graph_objects as go
#
# data_point = ['bitcoin-attack.v1.jani', 'breakdown-queues.v2.jani', 'dpm.v2.jani', 'erlang.v2.jani', 'ftwc.v3.jani']
# y1 = [54, 56, 56, 55, 57]
# y2 = [53, 56, 67, "ERROR", 55]
# y3 = [122, 124, 137, 125, 124]
# fig = go.Figure(data=[
#     go.Bar(name='MODES', x=data_point, y=y1, text=y1, textposition='auto', showlegend=True),
#     go.Bar(name='MCSTA', x=data_point, y=y2, text=y2, textposition='auto', showlegend=True),
#     go.Bar(name='STORM', x=data_point, y=y3, text=y3, textposition='auto', showlegend=True),
#
# ])
# # Change the bar mode
# fig.update_layout(barmode='group')
# fig.update_layout(title="MA Peak memory usage comparison")
# fig.update_layout(xaxis_title="MA Models")
# fig.update_layout(yaxis_title="peak memory usage")
# fig.write_image("fig1MA.png")

# import plotly.graph_objects as go
#
# data_point = ['consensus.2.v1.jani', 'csma.2-2.v1.jani', 'firewire.false.v2.jani', 'pacman.v1.jani',
# 'philosophers-mdp.3.v1.jani'] y1 = [56, 56, 57, 71, 56] y2 = [53, 54, 56, 67, 53] y3 = [122, 122, 125, 125,
# 121] fig = go.Figure(data=[ go.Bar(name='MODES', x=data_point, y=y1, text=y1, textposition='auto',
# showlegend=True), go.Bar(name='MCSTA', x=data_point, y=y2, text=y2, textposition='auto', showlegend=True),
# go.Bar(name='STORM', x=data_point, y=y3, text=y3, textposition='auto', showlegend=True),
#
# ])
# # Change the bar mode
# fig.update_layout(barmode='group')
# fig.update_layout(title="MDP Peak memory usage comparison")
# fig.update_layout(xaxis_title="MDP Models")
# fig.update_layout(yaxis_title="peak memory usage")
# fig.write_image("fig1MDP.png")

# import plotly.graph_objects as go
#
# data_point = ['bitcoin-attack.v1.modest', 'breakdown-queues.v2.modest', 'dpm.v2.modest', 'erlang.v2.modest',
# 'ftwc.v3.modest'] y1 = [55, 57, "ERROR", "ERROR", "ERROR"] y2 = [54, 56, "ERROR", "ERROR", "ERROR"] y3 = [122, 122,
# 125, 125, 121] fig = go.Figure(data=[ go.Bar(name='MODES', x=data_point, y=y1, text=y1, textposition='auto',
# showlegend=True), go.Bar(name='MCSTA', x=data_point, y=y2, text=y2, textposition='auto', showlegend=True),
# go.Bar(name='STORM', x=data_point, y=y3, text=y3, textposition='auto', showlegend=True),
#
# ])
# # Change the bar mode
# fig.update_layout(barmode='group')
# fig.update_layout(title="MA Peak memory usage comparison")
# fig.update_layout(xaxis_title="MA Models")
# fig.update_layout(yaxis_title="peak memory usage")
# fig.write_image("fig1MAmodest.png")


import plotly.graph_objects as go

data_point = ['cluster.v1', 'embedded.v1', 'fms.v1', 'kanban.v1', 'polling.12.v1', 'brp.v1', 'crowds.v1', 'egl.v1',
              'herman.3.v1', 'leader_sync.3-2.v1', 'consensus.2.v1', 'csma.2-2.v1', 'firewire.false.v2', 'pacman.v1',
              'philosophers-mdp.3.v1']
y1 = [122, 123, 122, 125, 193, 122, 122, 130, 109, 122, 122, 122, 125, 125, 121]
y2 = [148, 149, 149, 152, 221, 149, 149, 155, 135, 148, 148, 149, 151, 151, 148]
# y3 = [122, 122, 125, 125, 121]
fig = go.Figure(data=[
    go.Bar(name='JANI', x=data_point, y=y1, text=y1, textposition='auto', showlegend=True),
    go.Bar(name='PRISM', x=data_point, y=y2, text=y2, textposition='auto', showlegend=True),
    # go.Bar(name='STORM', x=data_point, y=y3, text=y3, textposition='auto', showlegend=True),

])
# Change the bar mode
fig.update_layout(barmode='group')
fig.update_layout(title="STORM Tool Peak memory usage comparison on different file input types")
fig.update_layout(xaxis_title="Models")
fig.update_layout(yaxis_title="peak memory usage")
fig.write_image("fig1StormPeakMemory.png", width=1980, height=1080)
