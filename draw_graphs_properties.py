import plotly.graph_objects as go
import pandas as pd
import math
csv_path = '/home/asif/PycharmProjects/PECSS/csvs/MODEL_PROPERTIES-PECSS-Sheet1.csv'
df = pd.read_csv(csv_path)
print(df.head())


def return_float_or_string(s):
    try:
        epmc_value = float(s)
        if math.isnan(epmc_value):
            epmc_value = float(0.0)
    except:
        epmc_value = float(0.0)
    return epmc_value


def get_dict_df(row):
    d = {"model_type": row[0], "file_name": row[1], "property": row[2], "storm_value": row[3], "epmc_value": row[4],
         "modes_value": row[5], "mcsta_value": row[6], "prism_value": row[7], "storm_time": row[9],
         "epmc_time": row[10], "modes_time": row[11], "mcsta_time": row[12], "prism_time": row[13]}
    return d


data_point = []
y_storm = []
y_strom_text = []
y_epmc = []
y_epmc_text = []
y_modes = []
y_modes_text = []
y_mcsta = []
y_mcsta_text = []
print("IMAGE 1")
for index, row in df.iterrows():
    if index > 2 and index < 43:
        d = get_dict_df(row)
        print(d)
        print("-" * 100)
        if index % 2 == 1 and index != 31:
            file_name = d['file_name'] + "-" + d['property']

            print(type(return_float_or_string(d['storm_value'])))
            maxx = max(return_float_or_string(d['storm_value']), return_float_or_string(d['modes_value']),
                       return_float_or_string(d['mcsta_value']))
            minn = min(return_float_or_string(d['storm_value']), return_float_or_string(d['modes_value']),
                       return_float_or_string(d['mcsta_value']))
            if minn > 0.0:
                # y_epmc.append(return_float_or_string(d['epmc_value']))
                print("type",type(return_float_or_string(d['storm_value'])),return_float_or_string(d['storm_value']))
                y_storm.append(return_float_or_string(d['storm_value']))
                y_modes.append(return_float_or_string(d['modes_value']))
                y_mcsta.append(return_float_or_string(d['mcsta_value']))
                data_point.append(file_name)
                # y_epmc[-1] = y_epmc[-1] / minn
                y_strom_text.append(y_storm[-1])
                y_modes_text.append(y_modes[-1])
                y_mcsta_text.append(y_mcsta[-1])
                # y_storm[-1] = y_storm[-1] / maxx
                # y_modes[-1] = y_modes[-1] / maxx
                # y_mcsta[-1] = y_mcsta[-1] / maxx
print("IMAGE 2. property values_(strom-mcsta-modes)")
print(data_point)
print(y_storm)
print(y_modes)
print(y_mcsta)
fig = go.Figure(data=[
    go.Bar(name='STORM', x=data_point, y=y_storm, text=y_storm,textposition='auto', showlegend=True),
    # go.Bar(name='EPMC', x=data_point, y=y_epmc, text=y_epmc_text, textposition='auto', showlegend=True),
    go.Bar(name='MODES', x=data_point, y=y_modes,text= y_modes, textposition='auto', showlegend=True),
    go.Bar(name='MCSTA', x=data_point, y=y_mcsta, text=y_mcsta ,textposition='auto', showlegend=True),
    # go.Bar(name='MODES', x=data_point, y=y3, text=y3, textposition='auto', showlegend=True),
])

# fig.update_layout(legend=dict(
#         x=0,
#         y=1,
#         traceorder='normal',
#         font=dict(
#             family='sans-serif',
#             size=12,
#             color='#000'
#         ),
#         bgcolor='#e5ecf6',
#     )
# )
fig.update_layout(
    autosize=False,
    width=500,
    height=500,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=50,
        pad=1
    ),
)
fig.update_layout(barmode='group')
# fig.update_layout(title="Property values comparison on different tools")
fig.update_layout(xaxis_title="Model - Property")
fig.update_layout(yaxis_title="property values")
fig.write_image("2. property values_(strom-mcsta-modes).png", width=500, height=500)

data_point = []
y_storm = []
y_storm_text = []
y_epmc = []
y_epmc_text = []
y_prism = []
y_prism_text = []
odd = True
for index, row in df.iterrows():
    if index > 2 and index < 43:
        d = get_dict_df(row)
        print(d)
        print("-" * 100)
        if index % 2 == 0:
            file_name = d['file_name'] + "-" + d['property']

            print(type(return_float_or_string(d['storm_value'])))
            maxx = max(return_float_or_string(d['storm_value']), return_float_or_string(d['epmc_value']),
                       return_float_or_string(d['prism_value']))
            minn = min(return_float_or_string(d['storm_value']), return_float_or_string(d['epmc_value']),
                       return_float_or_string(d['prism_value']))
            if minn > 0.0:
                if odd == True:
                    odd = False
                    continue
                else:
                    odd = True
                # y_epmc.append(return_float_or_string(d['epmc_value']))
                y_storm.append(return_float_or_string(d['storm_value']))
                y_epmc.append(return_float_or_string(d['epmc_value']))
                y_prism.append(return_float_or_string(d['prism_value']))
                data_point.append(file_name)
                # y_epmc[-1] = y_epmc[-1] / minn
                y_storm_text.append(y_storm[-1])
                y_epmc_text.append(y_epmc[-1])
                y_prism_text.append(y_prism[-1])
                # y_storm[-1] = y_storm[-1] / maxx
                # y_epmc[-1] = y_epmc[-1] / maxx
                # y_prism[-1] = y_prism[-1] / maxx

print(data_point)
print(y_storm)

fig = go.Figure(data=[
    go.Bar(name='STORM', x=data_point, y=y_storm, text=y_storm_text, textposition='auto', showlegend=True),
    go.Bar(name='EPMC', x=data_point, y=y_epmc, text=y_epmc_text, textposition='auto', showlegend=True),
    go.Bar(name='PRISM', x=data_point, y=y_prism, text=y_prism_text, textposition='auto', showlegend=True),
])
# fig.update_layout(legend=dict(
#         x=0,
#         y=1,
#         traceorder='normal',
#         font=dict(
#             family='sans-serif',
#             size=12,
#             color='#000'
#         ),
#         bgcolor='#e5ecf6',
#     )
# )
fig.update_layout(
    autosize=False,
    width=700,
    height=500,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=10,
        pad=1
    ),
)
fig.update_layout(barmode='group')
# fig.update_layout(title="Property values comparison on different tools")
fig.update_layout(xaxis_title="Model - Property")
fig.update_layout(yaxis_title="property values")
fig.write_image("2. property values_(prism-storm-epmc).png", width=700, height=500)
##################################################################################################################

data_point = []
y_storm = []
y_storm_text = []
y_mcsta = []
y_mcsta_text = []


for index, row in df.iterrows():
    if index > 2 and index < 43:
        d = get_dict_df(row)
        print(d)
        print("-" * 100)
        if index % 2 == 1:
            file_name = d['file_name'] + "-" + d['property']

            print(type(return_float_or_string(d['storm_time'])))
            maxx = max(return_float_or_string(d['storm_time']), return_float_or_string(d['mcsta_time']))
            minn = min(return_float_or_string(d['storm_time']), return_float_or_string(d['mcsta_time']))
            if minn > 0.0 and maxx < 1.0:
                # y_epmc.append(return_float_or_string(d['epmc_value']))
                y_storm.append(return_float_or_string(d['storm_time']))
                y_mcsta.append(return_float_or_string(d['mcsta_time']))
                data_point.append(file_name)
                # y_epmc[-1] = y_epmc[-1] / minn
                y_storm_text.append(y_storm[-1])
                y_mcsta_text.append(y_mcsta[-1])

print(data_point)
print(y_storm)

fig = go.Figure(data=[
    go.Bar(name='STORM', x=data_point, y=y_storm, text=y_storm_text, textposition='auto', showlegend=True),
    go.Bar(name='MCSTA', x=data_point, y=y_mcsta, text=y_mcsta_text, textposition='auto', showlegend=True),
    # go.Bar(name='PRISM', x=data_point, y=y_prism, text=y_prism_text, textposition='auto', showlegend=True),
])

fig.update_layout(barmode='group')
fig.update_layout(title="Property time comparison on different tools")
fig.update_layout(xaxis_title="Model - Property")
fig.update_layout(yaxis_title="property time in seconds")
fig.write_image("CompareJaniTimeSmall.png", width=2040, height=1080)


data_point = []
y_storm = []
y_storm_text = []
y_mcsta = []
y_mcsta_text = []


for index, row in df.iterrows():
    if index > 2 and index < 43:
        d = get_dict_df(row)
        print(d)
        print("-" * 100)
        if index % 2 == 1:
            file_name = d['file_name'] + "-" + d['property']

            print(type(return_float_or_string(d['storm_time'])))
            maxx = max(return_float_or_string(d['storm_time']), return_float_or_string(d['mcsta_time']))
            minn = min(return_float_or_string(d['storm_time']), return_float_or_string(d['mcsta_time']))
            if minn > 0.0 and maxx >= 1.0:
                # y_epmc.append(return_float_or_string(d['epmc_value']))
                y_storm.append(return_float_or_string(d['storm_time']))
                y_mcsta.append(return_float_or_string(d['mcsta_time']))
                data_point.append(file_name)
                # y_epmc[-1] = y_epmc[-1] / minn
                y_storm_text.append(y_storm[-1])
                y_mcsta_text.append(y_mcsta[-1])

print(data_point)
print(y_storm)

fig = go.Figure(data=[
    go.Bar(name='STORM', x=data_point, y=y_storm, text=y_storm_text, textposition='auto', showlegend=True),
    go.Bar(name='MCSTA', x=data_point, y=y_mcsta, text=y_mcsta_text, textposition='auto', showlegend=True),
    # go.Bar(name='PRISM', x=data_point, y=y_prism, text=y_prism_text, textposition='auto', showlegend=True),
])

fig.update_layout(barmode='group')
# fig.update_layout(title="Property time comparison on different tools")
fig.update_layout(xaxis_title="Model - Property")
fig.update_layout(yaxis_title="property time in seconds")
fig.write_image("CompareJaniTimeLarge.png", width=700, height=500)

data_point = []
y_storm = []
y_storm_text = []
y_mcsta = []
y_mcsta_text = []

odd = True
for index, row in df.iterrows():
    if index > 2 and index < 43:
        d = get_dict_df(row)
        print(d)
        print("-" * 100)
        if index % 2 == 1:
            file_name = d['file_name'] + "-" + d['property']

            print(type(return_float_or_string(d['storm_time'])))
            maxx = max(return_float_or_string(d['storm_time']), return_float_or_string(d['mcsta_time']))
            minn = min(return_float_or_string(d['storm_time']), return_float_or_string(d['mcsta_time']))
            if minn > 0.0 and maxx < 1.0 :
                if odd == True:
                    odd = False
                    continue
                else:
                    odd = True
                # y_epmc.append(return_float_or_string(d['epmc_value']))
                y_storm.append(return_float_or_string(d['storm_time']))
                y_mcsta.append(return_float_or_string(d['mcsta_time']))
                data_point.append(file_name)
                # y_epmc[-1] = y_epmc[-1] / minn
                y_storm_text.append(y_storm[-1])
                y_mcsta_text.append(y_mcsta[-1])

print(data_point)
print(y_storm)

fig = go.Figure(data=[
    go.Bar(name='STORM', x=data_point, y=y_storm, text=y_storm_text, textposition='auto', showlegend=True),
    go.Bar(name='MCSTA', x=data_point, y=y_mcsta, text=y_mcsta_text, textposition='auto', showlegend=True),
    # go.Bar(name='PRISM', x=data_point, y=y_prism, text=y_prism_text, textposition='auto', showlegend=True),
])
fig.update_layout(legend=dict(
        x=0,
        y=1,
        traceorder='normal',
        font=dict(
            family='sans-serif',
            size=12,
            color='#000'
        ),
        bgcolor='#e5ecf6',
    )
)
fig.update_layout(
    autosize=False,
    width=1080,
    height=720,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=10,
        pad=1
    ),
)
fig.update_layout(barmode='group')
# fig.update_layout(title="Property time comparison on different tools")
fig.update_layout(xaxis_title="Model - Property")
fig.update_layout(yaxis_title="property time in seconds")
fig.write_image("CompareJaniTimeTotal.png", width=1080, height=720)



data_point = []
y_storm = []
y_storm_text = []
y_epmc = []
y_epmc_text = []
y_prism = []
y_prism_text = []

for index, row in df.iterrows():
    if index > 2 and index < 43:
        d = get_dict_df(row)
        print(d)
        print("-" * 100)
        if index % 2 == 0:
            file_name = d['file_name'] + "-" + d['property']

            print(type(return_float_or_string(d['storm_time'])))
            maxx = max(return_float_or_string(d['storm_time']), return_float_or_string(d['epmc_time']), return_float_or_string(d['prism_time']))
            minn = min(return_float_or_string(d['storm_time']), return_float_or_string(d['epmc_time']), return_float_or_string(d['prism_time']))
            if minn > 0.0 :
                # y_epmc.append(return_float_or_string(d['epmc_value']))
                y_storm.append(return_float_or_string(d['storm_time']))
                y_epmc.append(return_float_or_string(d['epmc_time']))
                y_prism.append(return_float_or_string(d['prism_time']))
                data_point.append(file_name)
                # y_epmc[-1] = y_epmc[-1] / minn
                y_storm_text.append(y_storm[-1])
                y_epmc_text.append(y_epmc[-1])
                y_prism_text.append(y_prism[-1])

print(data_point)
print(y_storm)

fig = go.Figure(data=[
    go.Bar(name='STORM', x=data_point, y=y_storm, text=y_storm_text, textposition='auto', showlegend=True),
    go.Bar(name='EPMC', x=data_point, y=y_epmc, text=y_epmc_text, textposition='auto', showlegend=True),
    go.Bar(name='PRISM', x=data_point, y=y_prism, text=y_prism_text, textposition='auto', showlegend=True),
])
fig.update_layout(legend=dict(
        x=0,
        y=1,
        traceorder='normal',
        font=dict(
            family='sans-serif',
            size=12,
            color='#000'
        ),
        bgcolor='#e5ecf6',
    )
)
fig.update_layout(
    autosize=False,
    width=1080,
    height=720,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=50,
        pad=1
    ),
)
fig.update_layout(barmode='group')
fig.update_layout(title="Property time comparison on different tools")
fig.update_layout(xaxis_title="Model - Property")
fig.update_layout(yaxis_title="property time in seconds")
fig.write_image("ComparePrismTime.png", width=1080, height=720)



data_point = []
y_storm = []
y_storm_text = []
y_epmc = []
y_epmc_text = []
y_prism = []
y_prism_text = []

for index, row in df.iterrows():
    if index > 2 and index < 43:
        d = get_dict_df(row)
        print(d)
        print("-" * 100)
        if index % 2 == 0:
            file_name = d['file_name'] + "-" + d['property']

            print(type(return_float_or_string(d['storm_time'])))
            maxx = max(return_float_or_string(d['storm_time']), return_float_or_string(d['epmc_time']), return_float_or_string(d['prism_time']))
            minn = min(return_float_or_string(d['storm_time']), return_float_or_string(d['epmc_time']), return_float_or_string(d['prism_time']))
            if minn > 0.0 and maxx < 1.0:
                # y_epmc.append(return_float_or_string(d['epmc_value']))
                y_storm.append(return_float_or_string(d['storm_time']))
                y_epmc.append(return_float_or_string(d['epmc_time']))
                y_prism.append(return_float_or_string(d['prism_time']))
                data_point.append(file_name)
                # y_epmc[-1] = y_epmc[-1] / minn
                y_storm_text.append(y_storm[-1])
                y_epmc_text.append(y_epmc[-1])
                y_prism_text.append(y_prism[-1])

print(data_point)
print(y_storm)

fig = go.Figure(data=[
    go.Bar(name='STORM', x=data_point, y=y_storm, text=y_storm_text, textposition='auto', showlegend=True),
    go.Bar(name='EPMC', x=data_point, y=y_epmc, text=y_epmc_text, textposition='auto', showlegend=True),
    go.Bar(name='PRISM', x=data_point, y=y_prism, text=y_prism_text, textposition='auto', showlegend=True),
])

fig.update_layout(barmode='group')
fig.update_layout(title="Property time comparison on different tools")
fig.update_layout(xaxis_title="Model - Property")
fig.update_layout(yaxis_title="property time in seconds")
fig.write_image("ComparePrismTimeSmall.png", width=2040, height=1080)



data_point = []
y_storm = []
y_storm_text = []
y_epmc = []
y_epmc_text = []
y_prism = []
y_prism_text = []

for index, row in df.iterrows():
    if index > 2 and index < 43:
        d = get_dict_df(row)
        print(d)
        print("-" * 100)
        if index % 2 == 0:
            file_name = d['file_name'] + "-" + d['property']

            print(type(return_float_or_string(d['storm_time'])))
            maxx = max(return_float_or_string(d['storm_time']), return_float_or_string(d['epmc_time']), return_float_or_string(d['prism_time']))
            minn = min(return_float_or_string(d['storm_time']), return_float_or_string(d['epmc_time']), return_float_or_string(d['prism_time']))
            if minn > 0.0 and maxx >= 1.0:
                # y_epmc.append(return_float_or_string(d['epmc_value']))
                y_storm.append(return_float_or_string(d['storm_time']))
                y_epmc.append(return_float_or_string(d['epmc_time']))
                y_prism.append(return_float_or_string(d['prism_time']))
                data_point.append(file_name)
                # y_epmc[-1] = y_epmc[-1] / minn
                y_storm_text.append(y_storm[-1])
                y_epmc_text.append(y_epmc[-1])
                y_prism_text.append(y_prism[-1])

print(data_point)
print(y_storm)

fig = go.Figure(data=[
    go.Bar(name='STORM', x=data_point, y=y_storm, text=y_storm_text, textposition='auto', showlegend=True),
    go.Bar(name='EPMC', x=data_point, y=y_epmc, text=y_epmc_text, textposition='auto', showlegend=True),
    go.Bar(name='PRISM', x=data_point, y=y_prism, text=y_prism_text, textposition='auto', showlegend=True),
])
fig.update_layout(legend=dict(
        x=0,
        y=1,
        traceorder='normal',
        font=dict(
            family='sans-serif',
            size=12,
            color='#000'
        ),
        bgcolor='#e5ecf6',
    )
)
fig.update_layout(
    autosize=False,
    width=700,
    height=500,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=10,
        pad=1
    ),
)
fig.update_layout(barmode='group')
# fig.update_layout(title="Property time comparison on different tools")
fig.update_layout(xaxis_title="Model - Property")
fig.update_layout(yaxis_title="property time in seconds")
fig.write_image("ComparePrismTimeLarge.png", width=700, height=500)


data_point = []
y_storm_jani = []
y_storm_text_jani = []
y_storm_prism = []
y_storm_text_prism = []
l = []
odd = True
for index, row in df.iterrows():
    if index > 2 and index < 43:
        d = get_dict_df(row)
        l.append(d)

        if index % 2 == 0:
            file_name = d['file_name'] + "-" + d['property']

            print(type(return_float_or_string(d['storm_time'])))
            maxx = max(return_float_or_string(d['storm_time']), return_float_or_string(d['epmc_time']), return_float_or_string(d['prism_time']))
            minn = min(return_float_or_string(d['storm_time']), return_float_or_string(d['epmc_time']), return_float_or_string(d['prism_time']))
            if minn > 0.0 and maxx >= 1.0:

                # y_epmc.append(return_float_or_string(d['epmc_value']))
                y_storm.append(return_float_or_string(d['storm_time']))
                y_epmc.append(return_float_or_string(d['epmc_time']))
                y_prism.append(return_float_or_string(d['prism_time']))
                data_point.append(file_name)
                # y_epmc[-1] = y_epmc[-1] / minn
                y_storm_text.append(y_storm[-1])
                y_epmc_text.append(y_epmc[-1])
                y_prism_text.append(y_prism[-1])


for i in range(0,len(l),2):
    d1 = l[i]
    d2 =l[i+1]
    # print("dd",d1,d2)
    file_name = d1['file_name'].replace(".jani","") + "-" + d['property']
    storm_v1 = return_float_or_string(d1['storm_time'])
    storm_v2 = return_float_or_string(d2['storm_time'])
    print(storm_v1,storm_v2)
    if storm_v2 > 0.0:
        if odd == True:
            odd = False
            continue
        else:
            odd = True
        data_point.append(file_name)
        y_storm_jani.append(storm_v1)
        y_storm_prism.append(storm_v2)


# print(data_point)
# print(y_storm)

fig = go.Figure(data=[
    go.Bar(name='JANI', x=data_point, y=y_storm_jani, text=y_storm_jani, textposition='auto', showlegend=True),
    go.Bar(name='PRISM', x=data_point, y=y_storm_prism, text=y_storm_prism, textposition='auto', showlegend=True),
    # go.Bar(name='PRISM', x=data_point, y=y_prism, text=y_prism_text, textposition='auto', showlegend=True),
])
#
fig.update_layout(
    autosize=False,
    width=700,
    height=500,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=10,
        pad=1
    ),
)
fig.update_layout(barmode='group')
# fig.update_layout(title="Property time comparison on STORM on different input types")
fig.update_layout(xaxis_title="Model - Property")
fig.update_layout(yaxis_title="property time in seconds")
fig.write_image("STORM_COMPARE_TIME.png", width=700, height=500)







data_point = []
y_storm_jani = []
y_storm_text_jani = []
y_storm_prism = []
y_storm_text_prism = []
l = []
for index, row in df.iterrows():
    if index > 2 and index < 43:
        d = get_dict_df(row)
        l.append(d)

        if index % 2 == 0:
            file_name = d['file_name'] + "-" + d['property']

            print(type(return_float_or_string(d['storm_time'])))
            maxx = max(return_float_or_string(d['storm_time']), return_float_or_string(d['epmc_time']), return_float_or_string(d['prism_time']))
            minn = min(return_float_or_string(d['storm_time']), return_float_or_string(d['epmc_time']), return_float_or_string(d['prism_time']))
            if minn > 0.0 and maxx >= 1.0:
                # y_epmc.append(return_float_or_string(d['epmc_value']))
                y_storm.append(return_float_or_string(d['storm_time']))
                y_epmc.append(return_float_or_string(d['epmc_time']))
                y_prism.append(return_float_or_string(d['prism_time']))
                data_point.append(file_name)
                # y_epmc[-1] = y_epmc[-1] / minn
                y_storm_text.append(y_storm[-1])
                y_epmc_text.append(y_epmc[-1])
                y_prism_text.append(y_prism[-1])


for i in range(0,len(l),2):
    d1 = l[i]
    d2 =l[i+1]
    # print("dd",d1,d2)
    file_name = d1['file_name'].replace(".jani","") + "-" + d['property']
    storm_v1 = return_float_or_string(d1['storm_time'])
    storm_v2 = return_float_or_string(d2['storm_time'])
    print(storm_v1,storm_v2)
    if storm_v2 > 0.0 and storm_v2 < 1.0:
        data_point.append(file_name)
        y_storm_jani.append(storm_v1)
        y_storm_prism.append(storm_v2)


# print(data_point)
# print(y_storm)

fig = go.Figure(data=[
    go.Bar(name='JANI', x=data_point, y=y_storm_jani, text=y_storm_jani, textposition='auto', showlegend=True),
    go.Bar(name='PRISM', x=data_point, y=y_storm_prism, text=y_storm_prism, textposition='auto', showlegend=True),
    # go.Bar(name='PRISM', x=data_point, y=y_prism, text=y_prism_text, textposition='auto', showlegend=True),
])
#
fig.update_layout(barmode='group')
fig.update_layout(title="Property time comparison on STORM on different input types")
fig.update_layout(xaxis_title="Model - Property")
fig.update_layout(yaxis_title="property time in seconds")
fig.write_image("STORM_COMPARE_TIME_SMALL.png", width=2040, height=1080)




data_point = []
y_storm_jani = []
y_storm_text_jani = []
y_storm_prism = []
y_storm_text_prism = []
l = []
for index, row in df.iterrows():
    if index > 2 and index < 43:
        d = get_dict_df(row)
        l.append(d)

        if index % 2 == 0:
            file_name = d['file_name'] + "-" + d['property']

            print(type(return_float_or_string(d['storm_time'])))
            maxx = max(return_float_or_string(d['storm_time']), return_float_or_string(d['epmc_time']), return_float_or_string(d['prism_time']))
            minn = min(return_float_or_string(d['storm_time']), return_float_or_string(d['epmc_time']), return_float_or_string(d['prism_time']))
            if minn > 0.0 and maxx >= 1.0:
                # y_epmc.append(return_float_or_string(d['epmc_value']))
                y_storm.append(return_float_or_string(d['storm_time']))
                y_epmc.append(return_float_or_string(d['epmc_time']))
                y_prism.append(return_float_or_string(d['prism_time']))
                data_point.append(file_name)
                # y_epmc[-1] = y_epmc[-1] / minn
                y_storm_text.append(y_storm[-1])
                y_epmc_text.append(y_epmc[-1])
                y_prism_text.append(y_prism[-1])


for i in range(0,len(l),2):
    d1 = l[i]
    d2 =l[i+1]
    # print("dd",d1,d2)
    file_name = d1['file_name'].replace(".jani","") + "-" + d['property']
    storm_v1 = return_float_or_string(d1['storm_time'])
    storm_v2 = return_float_or_string(d2['storm_time'])
    print(storm_v1,storm_v2)
    if storm_v2 > 0.0 and storm_v2 >= 1.0:

        data_point.append(file_name)
        y_storm_jani.append(storm_v1)
        y_storm_prism.append(storm_v2)


# print(data_point)
# print(y_storm)

fig = go.Figure(data=[
    go.Bar(name='JANI', x=data_point, y=y_storm_jani, text=y_storm_jani, textposition='auto', showlegend=True),
    go.Bar(name='PRISM', x=data_point, y=y_storm_prism, text=y_storm_prism, textposition='auto', showlegend=True),
    # go.Bar(name='PRISM', x=data_point, y=y_prism, text=y_prism_text, textposition='auto', showlegend=True),
])
#
fig.update_layout(barmode='group')
fig.update_layout(title="Property time comparison on STORM on different input types")
fig.update_layout(xaxis_title="Model - Property")
fig.update_layout(yaxis_title="property time in seconds")
fig.write_image("STORM_COMPARE_TIME_LARGE.png", width=2040, height=1080)