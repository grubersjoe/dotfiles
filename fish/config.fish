if status is-interactive
    fish_add_path ~/.local/bin/
    fish_add_path ~/.go/bin

    set -Ux GOPATH ~/.go
end