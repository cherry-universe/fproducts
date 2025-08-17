#!/usr/bin/python
import sys
def gen_context(filename):
    template = """<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>{title}</title>
<link href="{cssfile}" rel="stylesheet" type="text/css">
</head>
 
<body>
{context}
</body>
</html>"""
    template_body = """<div class="title-layout">
		<h3 class="title-style">{}</h3>
	</div>
	<div class="main-layout">
		<div class="second-node">
		{}
		</div>
	</div>"""
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    file_context = ""
    title = ""
    cssfile = "../style/base.css"
    for line in lines:
        lst = line.split(' ')
        if lst[0] == "p":
            file_context += "<p>{}</p>".format(lst[1].strip())
        elif lst[0] == "img":
            file_context += "<img class=\"third-node\" src=\"{}\" alt=\"图片加载失败\">".format(lst[1].strip())
        elif lst[0] == "title":
            title = lst[1].strip()
        elif lst[0] == "css":
            cssfile = lst[1].strip()
    return template.format(title = title, cssfile = cssfile, context = template_body.format(title, file_context))

def gen_link(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    for line in lines:
        lst = line.split(' ')
        if lst[0] == "title":
            title = lst[1].strip()
    return "<a href=\"{}.html\"><button>{}</button></a>".format(filename, title)

for i in range(1, len(sys.argv)):
    file = open(sys.argv[i] + ".html", "w")
    all_context = gen_context(sys.argv[i])
    file.write(all_context)
    file.close()
    print(gen_link(sys.argv[i]))
