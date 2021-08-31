import click
from flask import Flask
import os

app = Flask(__name__)

@app.cli.command("gen-files")
@click.argument("title")
@click.argument("stylesheet")
@click.argument("script")
@click.argument("file")
@click.argument("lang")
def gen_files(title, stylesheet, script, file, lang):
    def gen_html(title, stylesheet, script, file, lang):
        head_string = f"""
        <head>
            <title>{title}</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            """
        
        if stylesheet:
            head_string += (f"<link rel=\"stylesheet\" href=\"{stylesheet}\">")
        if script:
            if stylesheet:
                head_string += "\n"
            head_string += (f"\t\t<script src=\"{script}\"></script>")
        head_string += "\n\t</head>\n\t"

        html_string = f"<!DOCTYPE html>\n<html lang=\"{lang}\">" + head_string + "<body>\n\t\t\n\t</body>\n</html>"

        with open("templates/" + file, "w") as f:
            f.write(html_string)

    # Make required dirs
    os.makedirs("static")
    os.makedirs("templates")

    # Generate HTML
    gen_html(file, title, stylesheet, script, lang)

    # Create CSS file
    with open("static/styles.css", "x") as f:
        f.write(":root {\n\t\n}")

    # Create JS file
    with open("static/script.js", "w") as f:
        f.write("window.onload = function() {\n\t\n}")

    # Write code to load index.html in main file
    with open("app.py", "w") as f:
        f.write(
            """\
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

app.run("0.0.0.0")"""
        )


app.cli.add_command(gen_files)