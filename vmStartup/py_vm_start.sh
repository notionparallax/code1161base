function explain() {
	MYTEXT='\e[0;35m'
	NOCOLOUR='\e[0m' # No Color
	echo -e "\n${MYTEXT} $* ${NOCOLOUR}"
}

exists()
{
	command -v "$1" >/dev/null 2>&1
}

explain "Ready to install everything you need."
explain "Lets go!"

#git
explain "add ppa for git"
sudo apt-add-repository ppa:git-core/ppa -y #latest git

#node and npm - I think apt-get works for this (below)
if exists node; then
	explain "yay node!"
else
	explain "install npm and node"
	curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -
	sudo apt-get install -y nodejs
	sudo ln -s /usr/bin/nodejs /usr/bin/node
fi

sudo chown -R `whoami` /usr/lib/node_modules
sudo chown -R `whoami` ~/.npm
sudo chown -R `whoami` /usr/bin/npm
sudo npm install -g npm #sudo considered bad, but it works ¯\_(ツ)_/¯

#install things
explain "update ppa repositories"
sudo apt-get update
explain "install lots of things"
#I know you can install these things all in one command, but I'm hoping that many commands will be more robust to failure
#this REALLY ought to be in a loop
explain "arduino"
sudo apt -y install arduino
explain "build-essential"
sudo apt -y install build-essential
explain "bundler"
sudo apt -y install bundler
explain "cups"
sudo apt -y install cups
explain "curl"
sudo apt -y install curl
explain "gdebi-core"
sudo apt -y install gdebi-core
explain "git"
sudo apt -y install git
explain "imagemagick"
sudo apt -y install imagemagick
explain "libapparmor1"
sudo apt -y install libapparmor1
explain "ruby2.3" #check version wanted here: https://www.brightbox.com/docs/ruby/ubuntu/
sudo apt -y install ruby2.3
explain "ruby2.3-dev" #numbers must match above
sudo apt -y install ruby2.3-dev
explain "rubygems"
sudo apt -y install rubygems
explain "samba"
sudo apt -y install samba
explain "sl"
sudo apt -y install sl
explain "wget"
sudo apt -y install wget
explain "xvfb"
sudo apt -y install xvfb
explain "unzip"
sudo apt -y install unzip
explain "python-tk"
sudo apt install -y python-tk

# this cleans out the duplicates from the ppas.
# Something to do with the way that the google ppas are set up
# sudo apt-get install python3-apt ## already comes with the distro
# git clone https://github.com/davidfoerster/apt-remove-duplicate-source-entries.git
# sudo apt-remove-duplicate-source-entries/apt-remove-duplicate-source-entries.py -y
#off we go again

# explain "install hyper"
# sudo apt -y install icnsutils graphicsmagick xz-utils rpm libappindicator1 #for hyper
# wget "https://hyper-updates.now.sh/download/linux_deb"
# sudo dpkg --install linux_deb

if exists atom; then
	explain "yay atom!"
else
	explain "install atom"
	sudo apt -y install build-essential git libgnome-keyring-dev fakeroot rpm libx11-dev libxkbfile-dev
	curl -sL https://git.io/vwEIX
fi
# wget -O atomdeb https://atom.io/download/deb
# sudo dpkg --install atomdeb
# atom #run atom, I don't thing the chown line makes sense until first run.
# sleep 20s #let it get started
# # killall -w atom #this gets blocked by the confirmation, not sure how to solve
# sudo chown -R `whoami` /home/`whoami`/.atom

explain "install processing"
if [ ! -f ~/processing.tgz ]; then
	HERE=`pwd`
	cd
	wget -O  processing.tgz "http://download.processing.org/processing-3.2.3-linux64.tgz"
	tar xvfz processing.tgz
	cd $HERE
	echo "alias processing='~/processing-3.2.3/processing'" >> ~/.bashrc
fi

explain "install pip"
sudo apt -y install python-pip
sudo -H pip install --upgrade pip #probably not needed, but belt and braces

explain "install ipython and jupyter"
sudo apt -y install python2.7 python-pip python-dev
sudo apt -y install ipython ipython-notebook
sudo apt -y install python-bs4
sudo apt -y install python-html5lib
sudo apt-get -f install -y # does a tidy up, needed for some reason
sudo -H pip install jupyter
explain "add jupyter slideshows"
# from https://github.com/damianavila/RISE
sudo -H pip install RISE
sudo jupyter-nbextension install rise --py --sys-prefix
sudo jupyter-nbextension enable rise --py --sys-prefix

sudo apt-add-repository ppa:dperry/ppa-graphviz-test
sudo apt-get update
sudo apt-get -y autoremove graphviz
sudo apt -y install graphviz

#pip packages
explain "install pip packages"
sudo -H pip install matplotlib numpy scipy requests
sudo -H pip install flake8 flake8-docstrings hacking mock
sudo -H pip colorama

#gems
explain "install ruby gems"
# sudo gem install **gem names**

# explain "get Noto fonts"
# # from https://www.google.com/get/noto/help/install/
# curl -sL 'https://noto-website-2.storage.googleapis.com/pkgs/Noto-hinted.zip'
# unzip Noto-hinted.zip
# sudo mkdir -p /usr/share/fonts/opentype/noto
# sudo cp *otf  /usr/share/fonts/opentype/noto
# sudo fc-cache -f -v # optional

#atom plugins
explain "install atom plugins"
apm install autocomplete-python
apm install file-icons
apm install highlight-selected
apm install linter
apm install linter-flake8
apm install markdown-writer
apm install minimap
apm install minimap-highlight-selected
apm install monokai-seti
apm install open-recent
apm install pigments
apm install script
apm install seti-ui
apm install sort-lines
apm install todo-show
apm install zen

#upgrade things if they need it
explain "upgrade things if they need it"
sudo apt-get -f install -y # does a tidy up, needed for some reason
sudo apt-get update -y
sudo apt-get upgrade -y #disable for testing - takes a long time
sudo apt-get clean -y

sudo gem update -Nq --system #N no docs, q quiet

explain "do some tests"
python ../week1/pytest.py
atom
jupyter notebook &


explain "All done!"
