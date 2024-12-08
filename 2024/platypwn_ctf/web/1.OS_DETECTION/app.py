from flask import Flask, request, render_template, render_template_string
from ua_parser import user_agent_parser

app = Flask(__name__)

@app.route("/")
def home():
    user_agent = request.headers.get('User-Agent')
    try:
        parsed_string = user_agent_parser.Parse(user_agent)
        family = parsed_string['os']['family']
        user_agent_hint = render_template_string(user_agent)
        return render_template('index.html', os=family, user_agent=user_agent_hint)
    except Exception as e:
        return render_template('failure.html', error=str(e))
    
@app.route("/source")
def source():
    code = open(__file__).read()
    return render_template_string("<pre>{{ code }}</pre>", code=code)
    

if __name__ == "__main__":
    # No debug, that would be insecure!
    #app.run(debug=True)
    app.run()
