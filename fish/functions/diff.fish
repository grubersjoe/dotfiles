function diff --wraps='colordiff -y --width=$COLUMNS' --description 'alias diff=colordiff -y --width=$COLUMNS'
  colordiff -y --width=$COLUMNS $argv
end
