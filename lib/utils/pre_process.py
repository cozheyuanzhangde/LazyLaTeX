import re

def start(content):
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