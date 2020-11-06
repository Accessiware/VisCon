import datetime
import sys
import os
import pypandoc

if len(sys.argv) != 2:
	print(f"Usage: python {sys.argv[0]} version")
	sys.exit()

version = sys.argv[1]
date = '{0:%Y-%m-%d}'.format(datetime.datetime.now())

print("Building documentation")
print(f"Version: {version}")
print(f"Date: {date}")
print("")

gathered_documentation = f"""% VisCon documentation
% Thomas byskov Dalgaard; Nicklas Tegner; Accessiware
% (C) Copyright 2019-{datetime.datetime.now().year}, Accessiware, All rights reserved.\n\n"""

gathered_documentation += f"Last updated: {date} for VisCon version {version}.\n\n"

root = "documentation"
print("Gathering documentation")
for file in os.listdir(root):
	with open(os.path.join(root, file)) as f:
		gathered_documentation += f.read()
print("Done gathering documentation")

print("Converting markdown documentation to html")
pypandoc.convert_text(gathered_documentation, "html", "markdown-blank_before_blockquote-blank_before_header-escaped_line_breaks-grid_tables-multiline_tables+pipe_tables-simple_tables-space_in_atx_header-table_captions+tex_math_dollars+hard_line_breaks", ("-s", "--wrap=preserve", "--mathml", "-p", "--atx-headers"), "utf-8", "documentation.html")

print("Done")
sys.exit(0)
