if status is-interactive
    fish_add_path ~/.local/bin/
    fish_add_path ~/.go/bin

    set -Ux EDITOR hx
    set -Ux GOPATH ~/.go
    set -Ux HOMEBREW_NO_ENV_HINTS 1
end