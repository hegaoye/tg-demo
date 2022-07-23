import os
import tempfile
from typing import List

import plotly.graph_objects as go
import plotly.io as pio


def __draw_table(header_values: List[str], cell_values: List[list], fill_colors: List[list]) -> str:
    """
    根据数据画图表，并保存到临时目录下
    :return: 图片地址
    """
    fig = go.Figure(data=[go.Table(
        columnwidth=[25, 15],
        header=dict(values=header_values, line_color=["gray"], fill_color=["rgb(238,238,238)"], font=dict(size=11)),
        cells=dict(values=cell_values, line_color=["gray"], fill_color=fill_colors, font=dict(size=11)))])

    pio.kaleido.scope.default_width = 300
    pio.kaleido.scope.default_height = len(cell_values[0]) * 21
    # image_file = "/Users/watson/PycharmProjects/tg-demo2/images/a.jpg"
    image_file = os.path.join(tempfile.gettempdir(), f'trend.jpg')
    # image_file = os.path.join(tempfile.gettempdir(), f'{uuid.uuid4().hex}.jpg')
    fig.update_layout(margin_l=0, margin_r=0, margin_b=0, margin_t=0)
    fig.write_image(image_file, scale=10)
    return image_file


def trend_image(data: List[str]) -> str:
    """
    元数据整合
    :param data: 数据 [time,num]
    """
    c_time = []
    c0 = []
    c1 = []
    c2 = []
    c3 = []
    c4 = []
    c5 = []
    c6 = []
    c7 = []
    c8 = []
    c9 = []

    f0 = []
    f1 = []
    f2 = []
    f3 = []
    f4 = []
    f5 = []
    f6 = []
    f7 = []
    f8 = []
    f9 = []

    for i in range(30):
        c0.append('')
        c1.append('')
        c2.append('')
        c3.append('')
        c4.append('')
        c5.append('')
        c6.append('')
        c7.append('')
        c8.append('')
        c9.append('')
        f0.append("white")
        f1.append("white")
        f2.append("white")
        f3.append("white")
        f4.append("white")
        f5.append("white")
        f6.append("white")
        f7.append("white")
        f8.append("white")
        f9.append("white")

    i = -1
    for time, num_str in data:
        c_time.append(time)
        num = int(num_str)
        i += 1
        if num == 0:
            c0[i] = 0
            f0[i] = "rgb(168,241,241)"
        elif num == 1:
            c1[i] = 1
            f1[i] = "rgb(168,241,241)"
        elif num == 2:
            c2[i] = 2
            f2[i] = "rgb(168,241,241)"
        elif num == 3:
            c3[i] = 3
            f3[i] = "rgb(168,241,241)"
        elif num == 4:
            c4[i] = 4
            f4[i] = "rgb(168,241,241)"
        elif num == 5:
            c5[i] = 5
            f5[i] = "rgb(168,241,241)"
        elif num == 6:
            c6[i] = 6
            f6[i] = "rgb(168,241,241)"
        elif num == 7:
            c7[i] = 7
            f7[i] = "rgb(168,241,241)"
        elif num == 8:
            c8[i] = 8
            f8[i] = "rgb(168,241,241)"
        elif num == 9:
            c9[i] = 9
            f9[i] = "rgb(168,241,241)"

    return __draw_table(['', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ''],
                        [c_time, c0, c1, c2, c3, c4, c5, c6, c7, c8, c9],
                        ["rgb(238,238,238)", f0, f1, f2, f3, f4, f5, f6, f7, f8, f9])

data = [['19:00', '9'], ['19:02', '4'], ['19:04', '2'], ['19:06', '5'], ['19:08', '1'], ['19:10', '3'], ['19:12', '6'],
        ['19:14', '7'], ['19:16', '5'], ['19:18', '9'], ['19:20', '0'], ['19:22', '7'], ['19:24', '2'], ['19:26', '4'],
        ['19:28', '4'], ['19:30', '5'], ['19:32', '6'], ['19:34', '7'], ['19:36', '8'], ['19:38', '9'], ['19:40', '0'],
        ['19:42', '1'], ['19:44', '5'], ['19:46', '6'], ['19:48', '4'], ['19:50', '7'], ['19:52', '6'], ['19:54', '7'],
        ['19:58', '8']]

print(trend_image(data))
