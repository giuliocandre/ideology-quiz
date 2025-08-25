# ideology_quiz_vector.py
import math

def calculate_scores(answers):
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

def description(ideology): 
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


def nearest_neighbor(answers, ideology_vectors):
    """
    Finds the ideology whose vector is nearest to the user's answers
    using Euclidean distance.
    """
    nearest = None
    min_dist = float('inf')

    for ideology, vector in ideology_vectors.items():
        # Euclidean distance
        dist = math.sqrt(sum((a - v)**2 for a, v in zip(answers, vector)))
        if dist < min_dist:
            min_dist = dist
            nearest = ideology

    return nearest, min_dist

def cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(a ** 2 for a in vec1))
    magnitude2 = math.sqrt(sum(b ** 2 for b in vec2))
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    return dot_product / (magnitude1 * magnitude2)

def nearest_neighbor_cosine(answers, ideology_vectors):
    nearest = None
    max_similarity = -1
    for ideology, vector in ideology_vectors.items():
        similarity = cosine_similarity(answers, vector)
        if similarity > max_similarity:
            max_similarity = similarity
            nearest = ideology
    return nearest, max_similarity

def questions():
    questions = [
        "Q1: The government should guarantee equal access to education and healthcare so everyone has a fair start in life.",
        "Q2: People should succeed or fail mostly based on their talent and effort, not their social background.",
        "Q3: Even if inequality increases, it is acceptable as long as opportunities are open to everyone.",
        "Q4: Free competition and private entrepreneurship are the best engines of innovation.",
        "Q5: Public investment and state-led projects are essential for major innovation (e.g., healthcare, green technology).",
        "Q6: The state should strongly intervene to protect common goods like the environment, even at the cost of limiting individual or corporate freedom.",
        "Q7: Protecting individual freedom (speech, property, lifestyle choices) should be the government’s highest priority.",
        "Q8: High wealth inequality is dangerous for democracy and society, even if the economy grows.",
        "Q9: The state should provide broad welfare (pensions, unemployment aid, free healthcare) even if it requires high taxes.",
        "Q10: Essential sectors (energy, education, transport) should be collectively owned rather than left to private companies."
    ]
    return questions

def main():
    print("Welcome to the Ideology Quiz (Vector Version)!")
    print("Answer each question on a scale from 0 (strongly disagree) to 5 (strongly agree).\n")

    answers = []


    for q in questions():
        while True:
            try:
                ans = int(input(f"{q}\nYour answer (0-5): "))
                if 0 <= ans <= 5:
                    answers.append(ans)
                    break
                else:
                    print("Please enter a number between 0 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    ideology_vectors = calculate_scores(answers)
    nearest, distance = nearest_neighbor(answers, ideology_vectors)
    # Cosine similarity nearest neighbor
    nn_cosine, similarity = nearest_neighbor_cosine(answers, ideology_vectors)

    print(f"\n>>> Your closest ideology (nearest neighbor) is: {nearest} + {nn_cosine} <<<")


if __name__ == "__main__":
    main()
