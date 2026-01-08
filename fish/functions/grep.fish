function grep --wraps='grep --color=auto'
  command grep --color=auto $argv
end
