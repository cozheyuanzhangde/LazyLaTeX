import os

# path: './test/output.tex'
def build(generated, dir_path):
    tex_path = dir_path + "output.tex"
    if os.path.exists(tex_path):
        os.remove(tex_path)
    with open(tex_path, 'a') as tex_file:
        for line in generated:
            tex_file.write(line + '\n')