function uuidc
    uuidgen | string lower | tr -d '\n' | pbcopy $argv
end
