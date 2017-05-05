git config --global credential.helper 'cache --timeout=36000' #cache password for 150 minutes
git config --global color.ui auto #colour the output in git
git config --global core.editor "atom --wait"

sudo -H pip uninstall flake8
sudo -H pip install flake8
sudo -H pip install colorama
sudo -H pip install pydocstyle
sudo -H pip install pandas

sudo chmod 777 ~/.atom/packages/
# forgive me for what I'm about to do
apm upgrade
apm install autocomplete-python
apm install file-icons
apm install highlight-selected
apm install linter
apm install linter-ui-default
apm install busy-signal
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
