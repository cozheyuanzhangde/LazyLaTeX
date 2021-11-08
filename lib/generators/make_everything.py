from ..utils import parse_text

def generate_latex_code(ith, gen, code_path):
    gen.append(r"\textbf{Code Snippet " + str(ith+1) + "}")
    gen.append(r"\lstinputlisting[language=Python]")
    command = r"{" + code_path + r"}"
    gen.append(command)

def generate(generated, name, course_name, homework_name, questions, answers, codes):
    title = r"\lecture{" + course_name + r"}{" + homework_name + r"}{" + name + r"}"
    generated.append(title)
    generated.append(r"\bee")
    for i in range(0, len(questions)):
        question = r"\i" + r" " + questions[i]
        generated.append(question)
        generated.append(r"\begin{tcolorbox}")
        generated.append(parse_text.start(answers[i]))
        generated.append(r"\end{tcolorbox}")
    generated.append(r"\ene")
    generated.append(r"\leavevmode\newline")
    for i in range(0, len(codes)):
        generate_latex_code(i, generated, codes[i])
    generated.append(r"\end{document}")