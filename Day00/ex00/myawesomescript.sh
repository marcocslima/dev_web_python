#!/bin/sh

echo $(curl -I -L -s -o /dev/null -w %{url_effective} "$1")