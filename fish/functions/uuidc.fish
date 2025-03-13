function uuidc --wraps=uuidgen\ \|\ string\ lower\ \|\ \ tr\ -d\ \'\\n\'\ \|\ pbcopy --description alias\ uuidc=uuidgen\ \|\ string\ lower\ \|\ \ tr\ -d\ \'\\n\'\ \|\ pbcopy
    uuidgen | string lower | tr -d '\n' | pbcopy $argv
end
