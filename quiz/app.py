from flask import Flask, render_template, request, jsonify
from .quiz import calculate_scores, nearest_neighbor, nearest_neighbor_cosine, questions, description
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
        
        # Get ideology vectors
        ideology_vectors = calculate_scores(answers)
        
        # Calculate nearest neighbors
        euclidean_nearest, euclidean_distance = nearest_neighbor(answers, ideology_vectors)
        cosine_nearest, cosine_similarity = nearest_neighbor_cosine(answers, ideology_vectors)
        
        # Determine results
        if euclidean_nearest == cosine_nearest:
            results = [{
                'ideology': euclidean_nearest,
                'method': 'Both Euclidean Distance and Cosine Similarity',
                'description' : description(euclidean_nearest),
                'euclidean_distance': round(euclidean_distance, 3),
                'cosine_similarity': round(cosine_similarity, 3)
            }]
        else:
            results = [
                {
                    'ideology': euclidean_nearest,
                    'method': 'Euclidean Distance',
                    'description' : description(euclidean_nearest),
                    'euclidean_distance': round(euclidean_distance, 3),
                    'cosine_similarity': None
                },
                {
                    'ideology': cosine_nearest,
                    'method': 'Cosine Similarity',
                    'description' : description(cosine_nearest),
                    'cosine_similarity': round(cosine_similarity, 3),
                    'euclidean_distance': None
                }
            ]
        
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
