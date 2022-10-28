from flask import Flask, request, render_template
from stories import Story

app = Flask(__name__)
story = Story(
["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = story.generate(request.form)
        return render_template('index.html', story=text)
    prompts = story.prompts
    return render_template('index.html', prompts=prompts)






app.run(debug=True)