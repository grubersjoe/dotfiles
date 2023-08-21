# i3-gaps config

**[not complete yet]**

This is the heart of my Linux desktop and the configuration files I put the most work into. They are the result of several years of experimenting and trying all kind of different approaches to shape my optimal work environment based on the great [i3 tiling window manager](https://i3wm.org/). Nowadays I use **[i3-gaps](https://github.com/Airblader/i3)**, because I wanted to use some of the applied patches like a custom height of the i3bar (no gaps though).

You might notice the `build.sh` script. I use a nearly identical Arch Linux based setup at home and at work, but some things like the monitor setup need to be configured independently. Therefore the i3 config file is created dynamically on every startup by concatenating the base configuration file and host specific additions. These extra configuration files live in the `./hosts` directory and must be named excactly after the `hostname`.

### Required packages

I use the following programs in my setup. If you are on Arch Linux like myself, you can install all of below packages from the [AUR](https://aur.archlinux.org/ Arch Linux User Repository) easily:

* [`i3pystatus`](https://github.com/enkore/i3pystatus) – a powerful replacement for i3bar
* [`dmenu2`](https://bitbucket.org/melek/dmenu2) – fork of dmenu - an efficient dynamic menu for X
* [`clipmenu`](https://github.com/cdown/clipmenu) – simple clipboard manager using dmenu and xsel
* [`playerctl`](https://github.com/acrisci/playerctl) – command line utility to control media players

#### Optional

* [`xcwd`](https://github.com/schischi/xcwd) - X current working directory<br>
    *Used to open a terminal "from here"*

### Fonts

Typography is very important to me and I spent a lot of time selecting well-suited fonts for my i3 setup. In the past I used the great Fira Sans from Mozilla and the Menlo clone Meslo LG, but recently I switched to the Roboto font family both for sans-serif and monospaced usage:

* [**Roboto** {Sans, Condensed, Mono}](https://github.com/google/roboto) – Google's default font family for Android and Chrome OS
* [**Material Icons**](https://design.google.com/icons/) – Material Design icon font as well from Google used for icons in the status bar

Of course selecting fonts is mostly a question of personal taste.

## Colors

I'm a great fan of [Chris Kempson's](https://github.com/chriskempson) [**base16** project](http://chriskempson.com/projects/base16/) and use it everywhere in my setup. It enables you to build an overall very consistent visual desktop experience. `i3` itself, the terminal emulator and my preferred text editor  `vim` all use the same color theme. Currently I'm using `base16-ashes` (see `bashrc` and `vimrc` respectively).
