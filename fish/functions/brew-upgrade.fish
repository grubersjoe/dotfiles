function brew-upgrade
    # Workaround for mac OS behavior to auto-remove apps from the dock.
    # See https://github.com/Homebrew/homebrew-cask/issues/102721
    defaults export com.apple.dock /tmp/dock.defaults

    brew update && brew upgrade --greedy-auto-updates

    defaults import com.apple.dock /tmp/dock.defaults
    killall Dock
end
