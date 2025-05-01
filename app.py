from flask import Flask, request

app = Flask(__name__)

# Function to transform text based on selected tone (placeholder logic).
def humanize_text(text, tone, language):
    """
    Basic placeholder transformations for demonstration:
    - Formal: uppercase the text.
    - Expanded: duplicate the text.
    - Simple: lowercase the text.
    - Standard: unchanged.
    """
    if tone == "Formal":
        return text.upper()
    elif tone == "Expanded":
        return text + " " + text  # Simple way to 'expand' by repeating.
    elif tone == "Simple":
        return text.lower()
    else:
        # Standard tone: return text unchanged.
        return text

# Home page route with form for humanizing text.
@app.route("/", methods=["GET", "POST"])
def home():
    # Initialize default values.
    input_text = ""
    output_text = ""
    selected_tone = "Standard"
    selected_language = "English"

    if request.method == "POST":
        # Get form data submitted by the user.
        input_text = request.form.get("inputText", "")
        selected_tone = request.form.get("tone", "Standard")
        selected_language = request.form.get("language", "English")
        # Process the text using the humanize_text function.
        output_text = humanize_text(input_text, selected_tone, selected_language)

    # Prepare the 'selected' attribute for dropdown options.
    tone_options = {
        "Standard": "selected" if selected_tone == "Standard" else "",
        "Formal":   "selected" if selected_tone == "Formal" else "",
        "Expanded": "selected" if selected_tone == "Expanded" else "",
        "Simple":   "selected" if selected_tone == "Simple" else ""
    }
    language_options = {
        "English": "selected" if selected_language == "English" else "",
        "Hindi":   "selected" if selected_language == "Hindi" else "",
        "Spanish": "selected" if selected_language == "Spanish" else "",
        "French":  "selected" if selected_language == "French" else ""
    }

    # HTML content with embedded CSS and JavaScript.
    # Uses f-string formatting to insert the current form values.
    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Humanize Text</title>
    <style>
        /* Embedded CSS for styling (Tailwind-style look) */
        body {{ font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f9fafb; color: #333; }}
        header {{ background-color: #4c51bf; padding: 1rem; color: white; text-align: center; font-size: 2rem; }}
        nav a {{ margin: 0 1rem; color: #fafafa; text-decoration: none; font-weight: bold; }}
        nav a:hover {{ color: #e2e8f0; }}
        .container {{ max-width: 800px; margin: 2rem auto; padding: 1rem; background: white;
                     border-radius: 0.5rem; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        h1 {{ text-align: center; margin-bottom: 1rem; }}
        label {{ display: block; margin: 0.5rem 0 0.2rem; font-weight: bold; }}
        select, textarea {{ width: 100%; padding: 0.5rem; border: 1px solid #cbd5e0; border-radius: 0.25rem; }}
        textarea {{ resize: vertical; height: 100px; }}
        .button {{ margin-top: 1rem; background-color: #667eea; color: white; padding: 0.75rem 1.5rem;
                   border: none; border-radius: 0.375rem; cursor: pointer; transition: background-color 0.3s ease; }}
        .button:hover {{ background-color: #5a67d8; }}
        .button:active {{ transform: scale(0.98); }}
        #copyBtn, #deleteBtn {{ background-color: #48bb78; }}
        #copyBtn:hover, #deleteBtn:hover {{ background-color: #38a169; }}
        #copyBtn:active, #deleteBtn:active {{ transform: scale(0.98); }}
        @media (max-width: 600px) {{
            header {{ font-size: 1.5rem; }}
            .container {{ margin: 1rem; }}
        }}
    </style>
</head>
<body>
    <!-- Header and navigation links -->
    <header>Humanize Text Tool</header>
    <nav class="container">
        <a href="/">Home</a>
        <a href="/privacy">Privacy Policy</a>
        <a href="/contact">Contact</a>
    </nav>

    <!-- Main tool container -->
    <div class="container">
        <h1>Humanize Text</h1>
        <form method="POST" action="/">
            <label for="inputText">AI-Generated Text:</label>
            <textarea id="inputText" name="inputText" placeholder="Enter AI-generated text here...">{input_text}</textarea>

            <label for="tone">Select Tone:</label>
            <select id="tone" name="tone">
                <option value="Standard" {tone_options['Standard']}>Standard</option>
                <option value="Formal" {tone_options['Formal']}>Formal</option>
                <option value="Expanded" {tone_options['Expanded']}>Expanded</option>
                <option value="Simple" {tone_options['Simple']}>Simple</option>
            </select>

            <label for="language">Language (Placeholder):</label>
            <select id="language" name="language">
                <option value="English" {language_options['English']}>English</option>
                <option value="Hindi" {language_options['Hindi']}>Hindi</option>
                <option value="Spanish" {language_options['Spanish']}>Spanish</option>
                <option value="French" {language_options['French']}>French</option>
            </select>

            <!-- Humanize button submits the form -->
            <button type="submit" class="button">Humanize</button>
        </form>

        <!-- Output area for the humanized text -->
        <label for="outputText">Humanized Text:</label>
        <textarea id="outputText" readonly>{output_text}</textarea>

        <!-- Copy and Delete buttons -->
        <button id="copyBtn" type="button" class="button">Copy</button>
        <button id="deleteBtn" type="button" class="button">Delete</button>
    </div>

    <script>
        // Copy output to clipboard when the Copy button is clicked.
        document.getElementById('copyBtn').addEventListener('click', function() {{
            var outputText = document.getElementById('outputText').value;
            if(outputText) {{
                navigator.clipboard.writeText(outputText);
                alert('Copied to clipboard!');
            }}
        }});

        // Clear both input and output text when Delete button is clicked.
        document.getElementById('deleteBtn').addEventListener('click', function() {{
            document.getElementById('inputText').value = '';
            document.getElementById('outputText').value = '';
        }});

        // Button click animation (scale down on mousedown, scale up on mouseup).
        document.querySelectorAll('.button').forEach(function(btn) {{
            btn.addEventListener('mousedown', function() {{
                btn.style.transform = 'scale(0.96)';
            }});
            btn.addEventListener('mouseup', function() {{
                btn.style.transform = 'scale(1)';
            }});
        }});
    </script>
</body>
</html>
"""
    return html

# Privacy Policy page (placeholder content).
@app.route("/privacy")
def privacy():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 2rem; background-color: #f9fafb; color: #333; }
        header { background-color: #4c51bf; padding: 1rem; color: white; text-align: center; font-size: 1.5rem; }
        .container { max-width: 800px; margin: 2rem auto; background: white; padding: 1rem;
                     border-radius: 0.5rem; }
        nav a { color: #4c51bf; text-decoration: none; font-weight: bold; }
        nav a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <header>Privacy Policy</header>
    <nav class="container"><a href="/">&#8592; Back to Home</a></nav>
    <div class="container">
        <p><strong>Privacy Policy:</strong> This is a placeholder privacy policy. We do not collect any personal data.</p>
        <p>This page should contain information about how user data is handled.</p>
        <p>Please replace this with actual privacy policy content.</p>
    </div>
</body>
</html>
"""

# Contact page with a simple form.
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Retrieve form data (no real email is sent).
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        # Display a simple thank-you page.
        return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Submitted</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 2rem; background-color: #f9fafb; color: #333; }}
        header {{ background-color: #4c51bf; padding: 1rem; color: white; text-align: center; font-size: 1.5rem; }}
        .container {{ max-width: 800px; margin: 2rem auto; background: white; padding: 1rem; border-radius: 0.5rem; }}
    </style>
</head>
<body>
    <header>Contact Us</header>
    <div class="container">
        <p>Thank you, {name}! We have received your message and will get back to you shortly.</p>
        <p><a href="/">Back to Home</a></p>
    </div>
</body>
</html>
"""
    # GET request: show the contact form.
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 2rem; background-color: #f9fafb; color: #333; }
        header { background-color: #4c51bf; padding: 1rem; color: white; text-align: center; font-size: 1.5rem; }
        .container { max-width: 800px; margin: 2rem auto; background: white; padding: 1rem; border-radius: 0.5rem; }
        label { display: block; margin-top: 1rem; }
        input, textarea { width: 100%; padding: 0.5rem; border: 1px solid #cbd5e0; border-radius: 0.25rem; }
        textarea { height: 100px; resize: vertical; }
        .button { margin-top: 1rem; background-color: #667eea; color: white;
                   padding: 0.75rem 1.5rem; border: none; border-radius: 0.375rem; cursor: pointer; }
        .button:hover { background-color: #5a67d8; }
    </style>
</head>
<body>
    <header>Contact Us</header>
    <div class="container">
        <p>Please fill out the form below to contact us.</p>
        <form method="POST" action="/contact">
            <label for="name">Your Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Your Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="message">Your Message:</label>
            <textarea id="message" name="message" required></textarea>

            <button type="submit" class="button">Send Message</button>
        </form>
        <p><a href="/">&#8592; Back to Home</a></p>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    # Run the Flask development server (accessible at http://localhost:5000).
    app.run(debug=True, port=5000)
