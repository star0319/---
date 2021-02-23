from pyecharts import options as opts
from pyecharts.charts import Pie


x_data = ["诚信信用", "价格收费", "自身权利", "客服售后", "界面操作","便利方便","安全健康","环保绿色"]
y_data = [495, 222, 364, 1348, 453,284,392,141]
c = (
    Pie(init_opts=opts.InitOpts(width="1400px", height="700px"))

    .add(
        "",
        [list(z) for z in zip(x_data, y_data )],
        radius=["30%", "75%"],
        center=["50%", "50%"],
        rosetype="area",
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="互联网用户对于共享产品关注因素的对比"))
    .render("pie_rosetype.html")
)
