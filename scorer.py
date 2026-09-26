def judge(question, expects, answer, results) -> bool:
    """
    Judge the answer of a question.

    Args:
        question (str): The question to be judged.
        expects (list): The expected answers.
        answer (str): The answer to be judged.
        results (dict): The results of the judge.

    Returns:
        bool: True if the answer is correct, False otherwise.
    """
    if answer in expects:
        return True
    else:
        return False