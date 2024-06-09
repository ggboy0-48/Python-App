import json
import random

from config.setting import question_path


class util:
    def __init__(self):
        pass

    def log(self, func):
        pass

    def get_questions(self, ques_level: int = 1) -> list:
        with open(f'{question_path}/python_{ques_level}.json', 'r', encoding='utf-8') as f:
            all_question = json.load(f)
        return all_question

    def random_staff(self, staff: list) -> str:
        return random.choice(staff)

    def random_question(self, all_questions: list) -> dict:
        return random.choice(all_questions)

    def judge(self, question: dict, result: str) -> bool:
        pass


