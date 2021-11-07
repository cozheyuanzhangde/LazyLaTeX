import re
import sys
import os
def generate_latex_code(gen, code_path):
    gen.append(r"\begin{lstlisting}[basicstyle=\footnotesize\ttfamily, breaklines]")
    with open(code_path, 'r') as f:
        code = f.read()
        gen.append(code)
    gen.append(r"\end{lstlisting}")
    
def output_generated(gen):
    if os.path.exists('output.tex'):
        os.remove('output.tex')
    with open('output.tex', 'a') as output_file:
        for line in gen:
            output_file.write(line + '\n')

def pre_process(content):
    regex_name = r"myname\((.*?)\)"
    regex_course_name = r"coursename\((.*?)\)"
    regex_homework_name = r"homeworkname\((.*?)\)"
    regex_questions = r"question\((.*?)\)"
    regex_answers = r"answer\((.*?)\)"
    regex_codes = r"code\((.*?)\)"
    name = re.search(regex_name, content).group(1)
    course_name = re.search(regex_course_name, content).group(1)
    homework_name = re.search(regex_homework_name, content).group(1)
    questions = re.findall(regex_questions, content)
    answers = re.findall(regex_answers, content)
    codes = re.findall(regex_codes, content)
    return name, course_name, homework_name, questions, answers, codes

def main():
    with open(sys.argv[1], 'r') as f:
        content = f.read()
    name, course_name, homework_name, questions, answers, codes = pre_process(content)
    generated = []
    generated.append(r"\documentclass[fleqn]{article}")
    generated.append(r"\usepackage{graphicx}")
    generated.append(r"\usepackage{./mydefs}")
    generated.append(r"\usepackage{./notes}")
    generated.append(r"\usepackage{url}")
    generated.append(r"\usepackage{float}")
    generated.append(r"\usepackage{amsmath}")
    generated.append(r"\usepackage{listings}")
    generated.append(r"\usepackage{courier}")
    generated.append(r"\usepackage{subcaption}")
    generated.append(r"\usepackage{tcolorbox}")
    generated.append(r"\begin{document}")
    title = r"\lecture{" + course_name + r"}{" + homework_name + r"}{" + name + r"}"
    generated.append(title)
    generated.append(r"\bee")
    for i in range(0, len(questions)):
        question = r"\i" + r" " + questions[i]
        generated.append(question)
        generated.append(r"\begin{tcolorbox}")
        generated.append(answers[i])
        generated.append(r"\end{tcolorbox}")
    for code in codes:
        generate_latex_code(generated, code)
    generated.append(r"\ene")
    generated.append(r"\end{document}")
    output_generated(generated)

if __name__ == '__main__':
    main()