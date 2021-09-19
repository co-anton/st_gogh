#!/usr/bin/zsh

check_download_themes() {
  themes=$HOME/.config/terminal_colours
  [[ ! -d $themes ]] && mkdir $themes
  url=https://raw.githubusercontent.com/Mayccoll/Gogh/master/data/themes.json
  if [[ ! -f $themes ]]; then
    curl -s $url > $themes/colours.json
  fi
  echo "$themes/colours.json"
}


print_names() {
  colours="$1"
  i="1"
  for theme in `cat $colours | jq ".themes[].name"`; do
    echo "$i) $theme"
    i=$((i+1))
  done
}

choose_names() {
  tmptheme="/tmp/colourtheme"
  colours=`check_download_themes`
  print_names $colours | less
  echo "Choose theme number: "
  read choice
  choice=$((choice-1))
  theme=`cat $colours | jq ".themes[$choice]"`
  name=`echo $theme | jq ".name "`
  echo "Setting theme: $name"

  # Writing values to temp file
  colours=(black red green yellow blue purple cyan white brightBlack brightRed brightGreen brightYellow brightBlue brightPurple brightCyan brightWhite)
  echo "static const char *colorname[] = {" > $tmptheme
  echo "  /* Theme - $name */" >> $tmptheme
  for colour in $colours; do
    echo "  `echo $theme | jq .$colour`," >> $tmptheme
  done
  echo "  `echo "/* Other colours */"`" >> $tmptheme
  echo "  [255] = 0," >> $tmptheme
  echo "  \"#cccccc\"," >> $tmptheme
  echo "  \"#555555\"," >> $tmptheme
  echo "  `echo "/* Foreground and background colours */"`" >> $tmptheme
  echo "  `echo $theme | jq ."foreground"`," >> $tmptheme
  echo "  `echo $theme | jq ."background"`," >> $tmptheme
  echo "};" >> $tmptheme
}

find_config() { find $HOME -path '**/st/config.h'  }

find_code_replace() {
  config=`find_config`
  echo "Updating $config"
  cp "$config" "$config.bkp" # backup
  
  # Replace colourname
  echo $config
  colourname=`pcregrep -Mo "^static const char \*colorname\[\] = (\{([^{}]++|(?1))*\};)" $config`
  echo $colourname > /tmp/oldtheme
  ./replace.py /tmp/oldtheme /tmp/colourtheme $config

  # Replace bg/fg
  sed -i 's/defaultfg = .*/defaultfg = 258;/' $config
  sed -i 's/defaultbg = .*/defaultbg = 259;/' $config
}


choose_names && find_code_replace && echo "Recompile st and test new theme! To reverse changes do \"mv \"$config.bkp\" $config"
