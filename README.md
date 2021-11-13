# Stewart Engart's Personal Website

## Thought Process

The time has come to move my personal website from a Raspberry Pi 3B+ Apache2 server in my living room to Github Pages. 

My website has 4 main pages and then linked project pages. The use of Jinja2 and Markdown2 are required to create the project pages from markdown. I have avoided using any proprietary Javascript. The only Javascript included is for my audio player, analytics, and for some collapsibles and for some p5js doodles.

## Requirements

Python Requirements

- [Jinja2](https://pypi.org/project/Jinja2/)
- [Markdown2](https://pypi.org/project/markdown2/)

Javascript Requirements

- [Essential Audio](https://essential.audio)
- [Goat Counter](https://github.com/zgoat/goatcounter)

## How to add a new piece

```bash
./newPiece.sh
Title: Title
New folder made at pieces/Title
Instrumentation: Instrumentation
Year: Year
Duration: Duration
Program notes: Program notes
```

## How to build project pages

```bash
python3 script.py
```

