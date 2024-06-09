import tkinter as tk
from tkinter import ttk
from config.setting import level_mapping
from utils.util import util


def main():
    windows = tk.Tk()
    windows.title("Python 课堂小测")
    windows.geometry("800x600")
    return windows


def selected_level(windows):
    select_box = ttk.Combobox(windows)
    select_box['values'] = list(level_mapping.keys())
    select_box.current(0)
    select_box.pack(pady=20)
    return select_box


def start_button(windows, combobox):
    start = tk.Button(windows, text='开始', command=lambda: start_quiz(windows, combobox))
    start.pack(pady=10)


def get_questions(question_level):
    tool = util()
    return tool.get_questions(question_level)


def empty(windows):
    for widget in windows.winfo_children():
        widget.destroy()


def start_quiz(windows, select_box):
    level = select_box.get()
    question_level = level_mapping[level]
    questions = get_questions(question_level)
    begin(windows, questions)


def begin(windows, all_q):
    tool = util()
    question = tool.random_question(all_q)
    empty(windows)
    selected = tk.StringVar()

    new_frame = tk.Frame(windows)
    new_frame.pack(fill='both', expand=True)

    query = tk.Label(new_frame, text=question['q'])
    query.pack(pady=(20, 10))

    options = [question['a'], question['b'], question['c'], question['d']]
    count = 0
    for option in options:
        count += 1
        if count == 1:
            an = 'A'
        elif count == 2:
            an = 'B'
        elif count == 3:
            an = 'C'
        else:
            an = 'D'
        option_radio = tk.Radiobutton(new_frame, text=option, variable=selected, value=an)
        option_radio.pack()

    submit_button = tk.Button(new_frame, text='提交',
                              command=lambda: check_answer(windows, selected.get(), question, all_q))
    submit_button.pack(pady=(20, 10))


def check_answer(windows, selected_answer, question, all_q):
    if selected_answer == question['key']:
        # 如果答案正确，重新显示题目
        begin(windows, all_q)
    else:
        # 如果答案错误，显示解析和下一题按钮
        show_analysis(windows, question, all_q)


def show_analysis(windows, question, all_q):
    empty(windows)
    analysis_frame = tk.Frame(windows)
    analysis_frame.pack(fill='both', expand=True)

    analysis_text = tk.Label(analysis_frame, text=f"错误！答案是：{question['key']}\n解析：{question['an']}")
    analysis_text.pack(pady=(20, 10))

    next_button = tk.Button(analysis_frame, text='下一题', command=lambda: begin(windows, all_q))
    next_button.pack(pady=(20, 10))


if __name__ == '__main__':
    root = main()
    select_box = selected_level(root)
    start_button(root, select_box)
    root.mainloop()
