from typing import List

import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
from plotly.colors import n_colors

np.random.seed(1)


def draw_table(headers: List[str], cells: List[list]):
    """
    画表

    :param headers: header=dict(values=['A Scores', 'B Scores'])
    :param cells: cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]])
    :return:
    """
    colors = n_colors('rgb(255, 200, 200)', 'rgb(200, 0, 0)', 9, colortype='rgb')
    a = np.random.randint(low=0, high=9, size=10)
    print(a)
    a_c = np.array(colors)[a]
    print(a_c)
    b = np.random.randint(low=0, high=9, size=10)
    c = np.random.randint(low=0, high=9, size=10)

    c_time = ['19:00', '19:02', '19:04', '19:06', '19:08', '19:10', '19:12', '19:14', '19:16', '19:18']
    c0 = ['0']
    c1 = ['', '1']
    c2 = ['', '', '2']
    c3 = ['', '', '', '3']
    c4 = ['', '', '', '', '4']
    c5 = ['', '', '', '', '', '5']
    c6 = ['', '', '', '', '', '', '6']
    c7 = ['', '', '', '', '', '', '', '7']
    c8 = ['', '', '', '', '', '', '', '', '8']
    c9 = ['', '', '', '', '', '', '', '', '', '9']
    fig = go.Figure(
        data=[go.Table(header=dict(values=['', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
                                   line_color=["gray"],
                                   fill_color=["rgb(238,238,238)"]
                                   ),
                       cells=dict(values=[c_time,
                                          c0,
                                          c1,
                                          c2,
                                          c3,
                                          c4,
                                          c5,
                                          c6,
                                          c7,
                                          c8,
                                          c9],
                                  line_color=["gray"],
                                  fill_color=[["rgb(238,238,238)"],
                                              ["rgb(168,241,241)", "white"],
                                              ["white", "rgb(168,241,241)", "white"],
                                              ["white","white", "rgb(168,241,241)", "white"],
                                              ["white","white","white", "rgb(168,241,241)", "white"],
                                              ["white","white","white","white", "rgb(168,241,241)", "white"],
                                              ["white","white","white","white","white", "rgb(168,241,241)", "white"],
                                              ["white","white","white","white","white","white", "rgb(168,241,241)", "white"],
                                              ["white","white","white","white","white","white","white", "rgb(168,241,241)", "white"],
                                              ["white","white","white","white","white","white","white","white", "rgb(168,241,241)", "white"],
                                              ["white","white","white","white","white","white","white","white","white", "rgb(168,241,241)"],
                                              ],
                                  font=dict(size=11)))])
    pio.kaleido.scope.default_height = 300
    pio.kaleido.scope.default_height = 600
    # fig = go.Figure(data=[go.Table(header=dict(values=headers), cells=dict(values=cells))])
    image_file = "/Users/watson/PycharmProjects/tg-demo2/images/a.jpg"
    # image_file = os.path.join(tempfile.gettempdir(), f'{uuid.uuid4().hex}.jpg')
    print('write image to', image_file)
    # fig.update_layout(width=300, height=400)
    fig.add_layout_image(x=0, y=0)
    fig.write_image(image_file, scale=10)
    return image_file


draw_table(['列A', '列B'], [[100, 90, 80, 90], [95, 85, 75, 95]])
