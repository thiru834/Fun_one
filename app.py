from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # Render the index.html page with a button to redirect
    return render_template('index.html')

@app.route('/redirect')
def redirect_to_huggingface():
    # Redirect to the Hugging Face OOTDiffusion page
    return redirect("https://huggingface.co/spaces/levihsu/OOTDiffusion")

if __name__ == '__main__':
    app.run(debug=True)
