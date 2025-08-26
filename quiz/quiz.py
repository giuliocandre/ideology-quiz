# ideology_quiz_vector.py
import math
from typing import Dict, List, Tuple
from random import shuffle

question_weights = [5, 2, 2, 2, 4, 4, 3, 3, 4, 5]

def calculate_scores(answers: List[int]) -> Dict[str, List[int]]:
    """
    answers: list of 10 integers (0–5)
    returns: dictionary with ideology scores (weighted sums)
    """

    if len(answers) != 10:
        raise ValueError("You must provide exactly 10 answers.")

    # Weights matrix: ideal response vectors for each ideology
    weights = {
        "Classical Liberalism":    [1, 5, 4, 5, 1, 1, 5, 2, 1, 1],
        "Neoliberalism":           [1, 5, 5, 5, 1, 1, 5, 2, 1, 1],
        "Rawlsian Liberalism":     [5, 4, 2, 4, 4, 4, 4, 5, 4, 2],
        "Nordic Social Democracy": [5, 4, 2, 4, 5, 5, 4, 5, 5, 3],
        "Classical Marxism":       [5, 1, 1, 1, 5, 5, 1, 5, 5, 5]
    }

    return weights

def description(ideology: str) -> str: 
    descriptions = {
        "Classical Liberalism": (
            "Classical Liberalism values personal freedom above all. It believes in private property, limited government, "
            "and letting individuals pursue their own success. The idea is that everyone should have equal rights, "
            "and free markets will naturally create prosperity."
        ),
        "Neoliberalism": (
            "Neoliberalism emphasizes competition and free markets as the main drivers of growth. "
            "It supports privatization, minimal government intervention, and rewards merit, "
            "even if it leads to inequality, trusting that economic efficiency benefits everyone in the long run."
        ),
        "Rawlsian Liberalism": (
            "Rawlsian Liberalism focuses on fairness and equal opportunities. "
            "It supports meritocracy but ensures that structural disadvantages are corrected first. "
            "Personal freedom is important, but social policies help everyone start on a level playing field."
        ),
        "Nordic Social Democracy": (
            "Nordic Social Democracy combines a market economy with a strong welfare state. "
            "It aims to reduce inequality through public services like healthcare and education, "
            "protect common goods, and encourage merit while keeping society fair and secure."
        ),
        "Classical Marxism": (
            "Classical Marxism seeks to eliminate class divisions by putting major industries under collective control. "
            "It prioritizes equality and social welfare over individual wealth, aiming for a society where resources and power are shared."
        )
    }

    return descriptions.get(ideology)


def nearest_neighbor(answers: List[int], ideology_vectors: Dict[str, List[int]], question_weights: List[int], alpha: float = 0.5) -> Dict[str, float]:
    """
    Finds the ideology whose vector is nearest to the user's answers
    using an hybrid score based on Euclidean nd cosine similarity with a blend of alpha.

    alpha is 1 -> cosine similarity only
    alpha is 0 -> euclidean only
    """

    scores = {}

    for ideology, vector in ideology_vectors.items():
        # Euclidean distance
        dist = math.sqrt(sum(w * (a - v)**2 for a, v, w in zip(answers, vector, question_weights)))
        # Euclidean similarity
        eu_sim = 1 / (dist + 1)

        cos_sim = cosine_similarity(answers, vector)

        score = alpha * cos_sim + (1 - alpha) * eu_sim

        scores[ideology] = score
        
    return scores

def cosine_similarity(vec1: List[int], vec2: List[int]) -> float:
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(a ** 2 for a in vec1))
    magnitude2 = math.sqrt(sum(b ** 2 for b in vec2))
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    return dot_product / (magnitude1 * magnitude2)


def questions() -> List[Tuple[int, str]]:
    questions: List[Question] = [
        (1, "The government should guarantee equal access to education and healthcare so everyone has a fair start in life."),
        (2, "People should succeed or fail mostly based on their talent and effort, not their social background."),
        (3, "Even if inequality increases, it is acceptable as long as opportunities are open to everyone."),
        (4, "Free competition and private entrepreneurship are the best engines of innovation."),
        (5, "Public investment and state-led projects are essential for major innovation (e.g., healthcare, green technology)."),
        (6, "The state should strongly intervene to protect common goods like the environment, even at the cost of limiting individual or corporate freedom."),
        (7, "Protecting individual freedom (speech, property, lifestyle choices) should be the government’s highest priority."),
        (8, "High wealth inequality is dangerous for democracy and society, even if the economy grows."),
        (9, "The state should provide broad welfare (pensions, unemployment aid, free healthcare) even if it requires high taxes."),
        (10, "Essential sectors (energy, education, transport) should be collectively owned rather than left to private companies.")
    ]
    
    shuffle(questions)
    return questions

def main():
    print("Welcome to the Ideology Quiz (Vector Version)!")
    print("Answer each question on a scale from 0 (strongly disagree) to 5 (strongly agree).\n")

    answers = []


    for idx, q in questions():
        while True:
            try:
                ans = int(input(f"{q}\nYour answer (0-5): "))
                if 0 <= ans <= 5:
                    answers.append((idx, ans))
                    break
                else:
                    print("Please enter a number between 0 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    answers = [ans for _, ans in sorted(answers, key=lambda x: x[0])]
    ideology_vectors = calculate_scores(answers)
    scores = nearest_neighbor(answers, ideology_vectors, question_weights)

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    print("\n>>> Your ideological profile <<<")
    for ideology, score in ranked[:2]:
        print(f"{ideology:25s}: {score:.1f}%")

if __name__ == "__main__":
    main()
