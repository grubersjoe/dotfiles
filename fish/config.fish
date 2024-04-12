if status is-interactive
    fish_add_path ~/.local/bin/
    fish_add_path ~/.go/bin

    set -Ux EDITOR hx
    set -Ux GOPATH ~/.go
    set -Ux HOMEBREW_NO_ENV_HINTS 1

    set KUBECONFIG ""
    for f in ~/.kube/*.yaml
        set KUBECONFIG "$KUBECONFIG:$f"
    end
    set -Ux KUBECONFIG $(echo $KUBECONFIG | cut -c 2-)
end
