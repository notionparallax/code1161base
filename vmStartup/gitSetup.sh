function explain() {
  MYTEXT='\e[0;35m'
  NOCOLOUR='\e[0m' # No Color
  echo -e "\n${MYTEXT} $* ${NOCOLOUR}"
}

explain "set git variables"
source variables #get the variables from a file so that people don't need to come into this file
#git
git config --global user.name $MYNAME
git config --global user.email $MYEMAIL
git config --global credential.helper 'cache --timeout=36000' #cache password for 150 minutes
git config --global color.ui auto #colour the output in git
git config --global core.editor "atom --wait"
