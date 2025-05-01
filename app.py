# app.py

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def humanize_text(text, style, lang):
    """
    Apply simple transformations to simulate human-like text conversion.
    This is a stub/demo function with basic rules for each style.
    """
    # Trim whitespace
    result = text.strip()

    # Apply style transformations
    if style == 'Formal':
        # Add formal greeting and closing
        if not result.startswith("Dear"):
            result = "Dear Sir or Madam,\n\n" + result
        if not result.endswith("Sincerely."):
            result += "\n\nSincerely."
    elif style == 'Expanded':
        # Add explanatory phrase to expand content
        result = result + "\n\nIt is important to note that " + result.lower()
    elif style == 'Simple':
        # Replace some complex words with simpler synonyms
        replacements = {
            'utilize': 'use',
            'commence': 'begin',
            'endeavor': 'try',
            'subsequent': 'next',
            'approximately': 'about',
            'demonstrate': 'show',
            'assist': 'help',
            'numerous': 'many',
            'apologies': 'sorry',
            'purchased': 'bought'
        }
        for word, simple in replacements.items():
            result = result.replace(word, simple)
    # Standard: no additional changes beyond trimming

    # Note on languages: Real translation is not implemented here.
    # For non-English, prepend a note (as a placeholder).
    if lang != 'English':
        result = f"[Translation to {lang} not implemented] " + result

    return result

@app.route('/', methods=['GET'])
def index():
    """Render the main page with input form."""
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    """
    Receive text, style, and language from the client (JSON),
    apply humanize_text, and return the result as JSON.
    """
    data = request.get_json()
    text = data.get('text', '')
    style = data.get('style', 'Standard')
    language = data.get('language', 'English')

    result = humanize_text(text, style, language)
    return jsonify({'result': result})

@app.route('/privacy', methods=['GET'])
def privacy():
    """Render a basic Privacy Policy page."""
    return render_template('privacy.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    Handle the contact form. On GET, display form; on POST, show a thank-you message.
    """
    if request.method == 'POST':
        # In a real app, handle sending the message (e.g., email or database).
        return render_template('contact.html', success=True)
    return render_template('contact.html', success=False)

if __name__ == '__main__':
    # Run the app locally (debug mode for development)
    app.run(debug=True)
