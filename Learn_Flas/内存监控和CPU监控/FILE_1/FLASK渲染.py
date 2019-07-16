import random,psutil
from pyecharts import Gauge
from flask import Flask, render_template


app = Flask(__name__)

def getCPUState(interval=1):
    cpuCount = psutil.cpu_count()
    cpuPercent = psutil.cpu_percent(interval)
    return (str(cpuCount), str(cpuPercent))

@app.route("/")
def hello():
    s3d = scatter3d()
    # print(s3d.get_js_dependencies())
    return render_template('index.html',
                           myechart=s3d.render_embed(),
                           script_list=s3d.get_js_dependencies())



def scatter3d():
    ga = Gauge('CPU监控')
    ga.use_theme('roma')
    range_color = [
        '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
        '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    ga.add('CPU 核心数 {} '.format(getCPUState()[0]), 'CPU 使用率', getCPUState()[1],  visual_range_color=range_color)
    return ga



if __name__ == "__main__":
    #运行项目
    app.run(debug = True)
