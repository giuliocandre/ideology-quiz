# Quick Ideology Quiz

A modern web application that helps users discover their political ideology through a 10-question quiz. The app uses vector-based analysis to match user responses with predefined ideology profiles using both Euclidean distance and cosine similarity methods.

## Features

- **Modern UI**: Clean, responsive design with smooth animations
- **Dual Analysis**: Uses both Euclidean distance and cosine similarity for ideology matching
- **Real-time Results**: Instant feedback with detailed metrics
- **Mobile Friendly**: Responsive design that works on all devices

## Ideology Profiles

The quiz compares your answers against these 5 ideology profiles:
- Classical Liberalism
- Neoliberalism  
- Rawlsian Liberalism
- Nordic Social Democracy
- Classical Marxism

## Installation

1. **Clone or download the project files**
   ```bash
   # Make sure you have these files:
   # - app.py
   # - quiz.py
   # - requirements.txt
   # - templates/index.html
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   uv run app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

## How It Works

1. **Answer 10 Questions**: Rate your agreement (0-5) with political statements
2. **Vector Analysis**: Your answers are compared to ideology profiles using:
   - **Euclidean Distance**: Measures geometric distance between answer vectors
   - **Cosine Similarity**: Measures angular similarity between answer vectors
3. **Results**: Shows your closest matching ideology(ies) with detailed metrics

## Technical Details

- **Backend**: Flask web framework
- **Frontend**: HTML5, CSS3, JavaScript (vanilla)
- **Analysis**: Vector-based similarity matching
- **Styling**: Modern gradient design with smooth animations

## File Structure

```
ideology-quiz/
├── app.py              # Flask application
├── quiz.py             # Core quiz logic and analysis
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Web interface
└── README.md          # This file
```

## Usage

1. Start the application with `python app.py`
2. Open your browser to `http://localhost:5000`
3. Answer all 10 questions using the 0-5 rating scale
4. Click "Get My Results" to see your ideology match
5. Review the detailed metrics and methodology used

## Development

To modify the quiz:
- Edit questions in `quiz.py` (function `questions()`)
- Adjust ideology profiles in `quiz.py` (function `calculate_scores()`)
- Customize styling in `templates/index.html`
- Modify Flask routes in `app.py`
