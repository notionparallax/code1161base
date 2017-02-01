#!/bin/bash
clear
toilet "     CODE1161     "  --metal --font future
echo ""
toilet "Let's get started!"  --metal --font future
echo ""
echo "We need to make this computer be YOURS"
echo "We need a name for you and your computer, make it short or it'll take up a lot of space."
echo "My computer is called um and my name is ben, so I get ben@um:~$ as my command prompt."
echo ""
read -p "Enter a name for your computer:"  compname
read -p "Enter your Name: "  username
echo ""
toilet "$username@$compname~$"  --gay --font wideterm
echo ""
echo "what do you think? If you hate it, press ctrl+c and do this again"
read -p "otherwise, just press enter." sacrificial
hostnamectl set-hostname $compname


# toilet ascii12 --font ascii12 --gay
# toilet bigascii9 --font bigascii9 --gay
# toilet circle --font circle --gay
# toilet future --font future --gay
# toilet mono9 --font mono9 --gay
# toilet smascii9 --font smascii9 --gay
# toilet smmono12 --font smmono12 --gay
# toilet ascii9 --font ascii9 --gay
# toilet bigmono12 --font bigmono12 --gay
# toilet emboss2 --font emboss2 --gay
# toilet letter --font letter --gay
# toilet pagga --font pagga --gay
# toilet smblock --font smblock --gay
# toilet smmono9 --font smmono9 --gay
# toilet bigascii12 --font bigascii12 --gay
# toilet bigmono9 --font bigmono9 --gay
# toilet emboss --font emboss --gay
# toilet mono12 --font mono12 --gay
# toilet smascii12 --font smascii12 --gay
# toilet smbraille --font smbraille --gay
# toilet wideterm --font wideterm --gay
