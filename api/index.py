from flask import Flask, redirect, render_template
import re

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/search')
def keywords():
    return render_template('search.html')

@app.route('/search/<cmd>')
def search_route(cmd):

    pattern = r'(?<=\S)%20(?=\S)'

    cmd_up = re.sub(pattern, ' ', cmd)

    trimmed_cmd = cmd_up.split(' ')[0]
    print(f'You typed in {trimmed_cmd}')


    parts = cmd_up.split(' ', 1)
    
    if len(parts) > 1:
        remaining_cmd = parts[1]
    else:
        remaining_cmd = ''
    
    print(f'You typed in {remaining_cmd}')

    if trimmed_cmd == "tw":
        return redirect("https://x.com")

    if trimmed_cmd == "re":
        return redirect("https://old.reddit.com")

    if trimmed_cmd == "gh":
        return redirect("https://github.com")

    if trimmed_cmd == "go":
        return redirect("https://google.com/search?q=" + remaining_cmd)

    if trimmed_cmd == "yt":
        return redirect("https://youtube.com/results?search_query=" + remaining_cmd)

    if trimmed_cmd == "duck":
        return redirect("https://duckduckgo.com/?t=h_&q=" + remaining_cmd)

    if trimmed_cmd == "bing":
        return redirect("https://www.bing.com/search?q=" + remaining_cmd)

    
    return f"Command {cmd} not recognized."


if __name__ == '__main__':
    app.run(debug=True)
