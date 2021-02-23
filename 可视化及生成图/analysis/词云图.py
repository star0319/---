import pyecharts.options as opts
from pyecharts.charts import WordCloud


data = [
    ("卸载差评", "143"),
    ("投诉", "503"),
    ("担心", "32"),
    ("点赞", "89"),
    ("棒棒", "96"),
    ("诚信", "63"),
    ("杀熟", "10"),
    ("价格、收费、费用", "170"),
    ("便宜", "62"),
    ("客服", "1125"),
    ("保修、维修", "113"),
    ("出租车运营管理", "5"),
    ("理赔", "38"),
    ("界面操作", "453"),
    ("便利方便", "284"),
    ("安全健康", "392"),
    ("环保绿色", "941"),
    ("滴滴","151"),
    ("出行","1045"),
    ("押金","983"),
    ("哈啰","777"),
    ("ofo","491"),
    ("喜欢","628"),
    ("单车", "393"),
    ("网约", "2"),
    ("商机", "2"),
]


(
    WordCloud()
    .add(series_name="互联网用户对于共享产品的关注因素及印象分析", data_pair=data, word_size_range=[6, 66])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="互联网用户对于共享产品的关注因素及印象分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("basic_wordcloud.html")
)
