# -*- coding:utf-8 -*-
#__author__:langzi
#__blog__:www.langzi.fun
import psutil
from pyecharts import Gauge
#from pyecharts import options as opts

def getCPUState(interval=1):
    cpuCount = psutil.cpu_count()
    cpuPercent = psutil.cpu_percent(interval)
    return (str(cpuCount), str(cpuPercent))

# def gauge_color() -> Gauge:
#     c = (
#         Gauge()
#         .add(
#             "业务指标",
#             [("完成率", 55.5)],
#             axisline_opts=opts.AxisLineOpts(
#                 linestyle_opts=opts.LineStyleOpts(
#                     color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=30
#                 )
#             ),
#         )
#         .set_global_opts(
#             title_opts=opts.TitleOpts(title="Gauge-不同颜色"),
#             legend_opts=opts.LegendOpts(is_show=False),
#         )
#     )
#     return c

ga = Gauge('CPU监控')
ga.use_theme('roma')
ga.add('CPU 核心数 {} '.format(getCPUState()[0]),'CPU 使用率',getCPUState()[1])
ga.render('6.html')

