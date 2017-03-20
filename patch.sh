# edit these lines
MYNAME="Ben Doherty"
MYEMAIL="ben@notionparallax.co.uk"
# stop editing


# don't edit these lines
git config --global user.name $MYNAME
git config --global user.email $MYEMAIL
git config --global credential.helper 'cache --timeout=36000' #cache password for 150 minutes
git config --global color.ui auto #colour the output in git
git config --global core.editor "atom --wait"

#in case this sh has been run multiple times before
git config --global --replace-all user.email $MYEMAIL
git config --global --replace-all user.name $MYNAME

git config --list

apm install script
apm install linter
apm install linter-flake8

sudo pip install colorama

sudo pip uninstall flake8 -y
sudo pip install flake8==3.2.0

echo "Installing Tkinter..."
sudo apt-get install python-tk

echo
echo "That should have fixed the bugs"
