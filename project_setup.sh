#!/usr/bin/env bash
platform=`uname -i`

if [ $platform="aarch64" ]; then
    filename=pandoc-3.1.11-linux-arm64.tar.gz
elif [ $platform="x86_64" ]; then
    filename=pandoc-3.1.11-linux-amd64.tar.gz
fi

wget https://github.com/jgm/pandoc/releases/download/3.1.11/$filename

tar xzf $filename