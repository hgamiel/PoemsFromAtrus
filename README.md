# PoemsFromAtrus
Taking random sentences Atrus has said from Myst and turning them into prose.

This is a side project I started to help with learning Python since I'm a C++ gal. Please be forgiving. :)

## Instructions
1. Run "python atrus.py" via the command line. (Make sure you have Python installed!)
2. A poem is spit out in the console and into the output.txt file.
3. If you have Twitter API information, store it in a text file called "creds.txt" in the same directory as the script. The poem generated will be automatically tweeted. Store the information in the following order, each separated by a single newline: `CONSUMER_KEY`, `CONSUMER_SECRET`, `ACCESS_TOKEN_KEY`, `ACCESS_TOKEN_SECRET`.
4. That is all!

## Want to Contribute?
This is my first Python project and I would love to include contributions that would improve it! Please fork this project and create a pull request to appropriate branch based on what you are editing.

### Branches
- **Master:** Main branch. Please do not commit to this branch. Commit to the appropriate alternate branch and perform a pull request.
- **Generator:** Any edits to generator.py should be done in this branch.
- **Text:** Any edits to the output or input files should be done in this branch.
