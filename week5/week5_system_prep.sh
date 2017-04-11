git config --global credential.helper 'cache --timeout=36000' #cache password for 150 minutes
git config --global color.ui auto #colour the output in git
git config --global core.editor "atom --wait"

sudo pip uninstall flake8
sudo pip install flake8
sudo pip install colorama
sudo pip install pydocstyle

apm upgrade
apm install autocomplete-python
apm install file-icons
apm install highlight-selected
apm install linter
apm install linter-flake8
apm install linter-pydocstyle
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

echo
echo "Everything should be good now!"
