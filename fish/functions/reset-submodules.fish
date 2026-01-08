function reset-submodules --wraps='git submodule update --init'
    git submodule update --init $argv
end
