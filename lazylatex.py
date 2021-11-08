import sys

from lib.generators import initial
from lib.generators import make_everything
from lib.utils import pre_process
from lib.utils import tex_builder


def main():
    with open(sys.argv[1], 'r') as f:
        content = f.read()
    name, course_name, homework_name, questions, answers, codes = pre_process.start(content)
    generated = []
    initial.generate(generated)
    make_everything.generate(generated, name, course_name, homework_name, questions, answers, codes)
    tex_builder.build(generated, "./test")

if __name__ == '__main__':
    main()