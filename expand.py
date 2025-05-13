import re
def expand_input(tex_content):
    def replace_input(match):
        filename = match.group(1)
        with open(f'{filename}','r',encoding='utf-8') as f:
            return expand_input(f.read())
    return re.sub(r'\\input\{(.*?)\}',replace_input,tex_content)

with open('paper1.tex','r',encoding='utf-8') as f:
    content = f.read()

merged_content = expand_input(content)

with open('paper.tex','w',encoding='utf-8') as f:
    f.write(merged_content)