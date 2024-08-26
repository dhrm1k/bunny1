from flask import Flask, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/search/<cmd>')
def search_route(cmd):
    trimmed_cmd = cmd.split(' ')[0]
    print(f'You typed in {cmd}')

    parts = cmd.split(' ', 1)
    
    if len(parts) > 1:
        remaining_cmd = parts[1]  # Get everything after the first word (tw)
    else:
        remaining_cmd = ''  # If there's no "something else", it will be an empty string
    
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

    
    return f"Command {cmd} not recognized."


if __name__ == '__main__':
    app.run(debug=True)
