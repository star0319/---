from pyecharts import options as opts
import pyecharts.options as opts
from pyecharts.charts import Radar
data = [{"value": [1649, 775, 3629, 1299], "name": "第一阶段"}]

c_schema = [
    {"name":"非常不看好",  "max": 4000, "min": 0},
    {"name": "不看好", "max": 4000, "min": 0},
    {"name":"看好"  , "max": 4000, "min": 0},
    {"name": "非常看好", "max": 4000, "min": 0},

]
c = (
    Radar()
    .set_colors(["#4587E7"])
    .add_schema(
        schema=c_schema,
        shape="circle",
        center=["50%", "50%"],
        radius="80%",
        angleaxis_opts=opts.AngleAxisOpts(
            min_=0,
            max_=360,
            is_clockwise=False,
            interval=5,
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axislabel_opts=opts.LabelOpts(is_show=False),
            axisline_opts=opts.AxisLineOpts(is_show=False),
            splitline_opts=opts.SplitLineOpts(is_show=False),
        ),
        radiusaxis_opts=opts.RadiusAxisOpts(
            min_=4000,
            max_=0,
            interval=500,
            splitarea_opts=opts.SplitAreaOpts(
                is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
            ),
        ),
        polar_opts=opts.PolarOpts(),
        splitarea_opt=opts.SplitAreaOpts(is_show=False),
        splitline_opt=opts.SplitLineOpts(is_show=False),
    )
    .add(
        series_name="频数",
        data=data,
        areastyle_opts=opts.AreaStyleOpts(opacity=0.1),
        linestyle_opts=opts.LineStyleOpts(width=1),
    )
        .set_global_opts(title_opts=opts.TitleOpts(title="互联网用户对于共享产品前景持有的态度分析"))
    .render("radar_angle_radius_axis.html")
)
