#!/usr/bin/python
import sys
def gen_context(filename):
    template = """<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>{title}</title>
<link href={cssfile} rel="stylesheet" type="text/css">
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
    file_context = open(filename, "r")
    title = filename
    return template.format(title = title, cssfile = "../style/base.css", context = template_body.format(title, file_context.read()))

print(gen_context(sys.argv[1]))
