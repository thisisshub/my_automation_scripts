# My Automation Scripts



 How to make a Github Repo from command line using Github API.



## Usuage

Make an alias in `~/.bashrc` or `~/.zshrc`

with `alias create="python script.py"`  



What this Script does :-



	 1. makes a dir

	 2. cd into dir

	 3. git init && touch README.md && git add .git* && git commit -m "Initial commit"

	 4. hub creates a directory in github



I use `hub` as a repository creator you can use curl if you'd like 



```

curl -u 'your_github_username' https://api.github.com/user/repos -d "{\"name\":\"$repo_name\"}"

```








