function dcd --wraps='docker compose down'
    docker compose down $argv
end
