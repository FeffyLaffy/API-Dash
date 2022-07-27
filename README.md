# API Dash

First [Muse Dash](https://store.steampowered.com/app/774171/Muse_Dash/) Private Server made with flask (python).

## Features
- [] Custom leaderboard.
- [] login account (~~facebook~~, google, ~~qq/wechat~~ saving method no work).
- [x] Custom announcement.
- [x] Custom Music Tag.

## Supported platform
- [Windows](https://www.microsoft.com/en-us/windows). Tested with Windows 10 and 11.

## Requirements
- [CMake](https://cmake.org/).
- [Conan, the C/C++ Package Manager](https://conan.io). [CMake](https://cmake.org/) will install needed package with [Conan, the C/C++ Package Manager](https://conan.io/).
Required python >= 3.5
```shell
$ pip install conan
```

## Building the source
```shell
$ mkdir build
$ cd build
$ cmake .. -DCMAKE_BUILD_TYPE=Debug
$ cmake --build .
```

## For Growtopia version 3.91-3.93
- You need add `www.` before growtopia[1-2].com in `hosts` file.
```text
127.0.0.1 www.growtopia1.com
127.0.0.1 www.growtopia2.com
```

## Running the program
- If you on Windows, you need move needed dynamic binary from `/path/to/binary/conan/bin` to `/path/to/program/`.
- Run the program.
- Edit the `config.json` file.
- Run the program again.
- Enjoy.

## Credits
- Thanks to my two friends who helped a lot with this project.
