def judge(question, expects, answer, results) -> bool:
    """
    Judge the answer of a question.

    Args:
        question (str): The question asked.
        expects (str): A keyword/phrase a correct answer should contain.
        answer (str): The answer the system produced.
        results (list): The retrieved chunks for this question.

    Returns:
        bool: True if `expects` shows up in the answer, False otherwise.
    """
    if not expects:
        return False
    return expects.strip().lower() in answer.lower()
