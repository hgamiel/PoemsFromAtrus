# PoemsFromAtrus
Taking random sentences Atrus has said from Myst and turning them into prose.

This is a side project I started to help with learning Python since I'm a C++ gal. Please be forgiving. :)

## Instructions
1. Enter `classes` directory and run `python Program.py` via the command line. (Make sure you have Python installed!)
2. A "poem" is spit out in the console and into the output.txt file.
3. If you have Twitter API information, store it in a text file called "creds.txt" in the `textfiles` directory. The poem generated will be automatically tweeted. Store the information in the following order, each separated by a single newline: `CONSUMER_KEY`, `CONSUMER_SECRET`, `ACCESS_TOKEN_KEY`, `ACCESS_TOKEN_SECRET`. I use [TwitterAPI for Python](https://github.com/geduldig/TwitterAPI), which you will need to install via `pip install TwitterAPI`.
4. That is all!

## Want to Contribute?
This is my first Python project and I would love to include contributions that would improve it! Please fork this project and create a pull request to the appropriate branch based on what you are editing.

### Branches
- **Master:** Main branch. Please do not commit to this branch. Commit to the appropriate alternate branch and perform a pull request.
- **Generator:** Any edits to files in the `classes` directory should be done in this branch.
- **Text:** Any edits to the output or input files in the `textfiles` directory should be done in this branch.
