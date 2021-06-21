import mammoth

input_filename = "test.docx"

custom_styles = """ b => b.mark
                    u => u.initialism
                    p[style-name='Heading 1'] => h1.card
                    table => table.table.table-hover
                    """
with open(input_filename, "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file, style_map=custom_styles)
    html = result.value

edited_html = html

output_filename = "output.html"
with open(output_filename, "w") as f:
    f.writelines(edited_html)
