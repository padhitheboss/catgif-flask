from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
        "https://c.tenor.com/dur8_lWhH2cAAAAC/crazy-cat-dancing-crazy-cat.gif",
        "https://c.tenor.com/GTcT7HODLRgAAAAC/smiling-cat-creepy-cat.gif",
        "https://c.tenor.com/wSJZSQqIHhUAAAAC/love-cats-cat.gif",
        "https://c.tenor.com/tMRY35MWfYYAAAAM/funny-silly.gif",
        "https://c.tenor.com/qavWfVh55fsAAAAd/cat-cute-cat.gif",
        "https://c.tenor.com/I_DYaT5W9JkAAAAM/cat-stacked.gif",
        "https://c.tenor.com/dR2xz8F135QAAAAM/cat-cute.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
