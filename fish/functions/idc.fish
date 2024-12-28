function idc --wraps=uuidgen\ \|\ tr\ -d\ \'\\n\'\ \|\ pbcopy --description alias\ idc=uuidgen\ \|\ tr\ -d\ \'\\n\'\ \|\ pbcopy
    uuidgen | tr -d '\n' | pbcopy $argv
end
