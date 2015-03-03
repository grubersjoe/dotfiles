#!/usr/bin/env bash

# Not working yet
sqlite ~/.config/google-chrome/Default/History 'DELETE from urls WHERE url LIKE "%$1%";'
