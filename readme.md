### POEM GENERATOR

This project seems to create poems algorithmically based on structures and source material.

### Notes
1. These will have to be installed on your machine:
`apt-get install git python-virtualenv python-pip`

If there is a problem, or even not, might as well try to install some of the develeper python packages:
`apt-get install python-setuptools python-dev build-essential`


2. Create a github account

3. Create an ssh key on your machine and add it to your github account
- https://help.github.com/articles/generating-an-ssh-key/
- https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/

4. find a spot on your coputer where you want to place all your project files. If you open terminal and type
`cd ~` it will bring you to your home directory. In your home directory you can create an new directory called "project" by using the command: `cd ~/project`.

5. Move into your newly created directory by typing `cd ~/project`.

6. Create a little python environment where all the python files and libraries will live
- `virtualenv ~/project/venv`

7. Create a directory to place all your project source files. Move into the newly created directory.
- `cd ~/project/src; cd ~/project/src`

8. Clone this repository to your local envirnment.
  `git clone git@github.com:codydjango/poem.git ~/project/src/`

9. Activate the virtual environment you've created (it might be active already; you can activate it again)
- `source ~/project/venv/bin/activate`

10. Install the python dependencies (as listed in the python requirements.txt file included in our src code). So long as we have activated our python envirement, they will be installed into the activated python enviroment, and not our global envirement.
- `pip install -r ~/project/src/requirements.txt`


11. Once all the system and python dependencies have been met, we're good to try running the project.

12. nltk requires an extra download for the dictionary we're using. You'll need to do this step manually. open the python interpreter. 
`python -c "import nltk; nltk.download()"`
- http://www.nltk.org/install.html
- http://stackoverflow.com/questions/27658409/downloading-error-using-nltk-download

13. Once you have that library installed you should be all good to go! I'm probably still missing a whole tonne here so lemme know which steps don't make sense. Please reach out to me on fb or email or slack or wherever. But still at this point you should be able to run the poem script directly:
- `~/project/poem.py`


* git notes
git add * # to add all changes to index (stage the local changes)
git commit -m "message of the commit goes here" # to commit staged local changes
git push origin master # to push committed staged local changes to remote
- http://rogerdudler.github.io/git-guide/
- https://git-scm.com/book/en/v2/Getting-Started-Git-Basics











