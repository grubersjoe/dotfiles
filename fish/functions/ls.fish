function ls --wraps='gls -h --color --group-directories-first' --description 'alias ls=gls -h --color --group-directories-first'
    gls -h --color --group-directories-first $argv
end
