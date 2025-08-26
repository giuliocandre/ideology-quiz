from flask import Flask, render_template, request, jsonify
from .quiz import calculate_scores, nearest_neighbor, questions, description, question_weights
from pathlib import Path
import os

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main quiz page"""
    return render_template("index.html", questions=questions())

@app.route('/submit', methods=['POST'])
def submit_quiz():
    """Handle quiz submission and return results"""
    try:
        # Get answers from form
        answers = []
        for i in range(1, 11):  # 10 questions
            answer = request.form.get(f'q{i}')
            if answer is None:
                return jsonify({'error': f'Missing answer for question {i}'}), 400
            try:
                answer = int(answer)
                if not (0 <= answer <= 5):
                    return jsonify({'error': f'Invalid answer for question {i}. Must be 0-5.'}), 400
                answers.append(answer)
            except ValueError:
                return jsonify({'error': f'Invalid answer format for question {i}'}), 400
        
        answers = [ans for _, ans in sorted(answers, key=lambda x: x[0])]

        # Get ideology vectors
        ideology_vectors = calculate_scores(answers)
        
        # Calculate nearest neighbors
        scores = nearest_neighbor(answers, ideology_vectors, question_weights)
        # cosine_nearest, cosine_similarity = nearest_neighbor_cosine(answers, ideology_vectors)
        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        
        results = []
        for ideology, score in ranked[:2]:
            results.append({
                'ideology': ideology,
                'method': 'Both Euclidean Distance and Cosine Similarity',
                'description' : description(ideology),
                'score': f"{score:.1f}%",
            })

        return jsonify({
            'success': True,
            'results': results,
            'answers': answers
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def main():
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=8000)
