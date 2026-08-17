# Ping Pong

Two-player Pong, built with Python's `turtle` graphics module.

[![Python](https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/) [![Turtle](https://img.shields.io/badge/turtle-graphics-2ea44f?style=flat-square)](https://docs.python.org/3/library/turtle.html)

---

## Play

```bash
git clone https://github.com/dhruvg0ya1/Ping-Pong-Game.git
cd Ping-Pong-Game
python Main.py
```

| Player | Up | Down |
|---|---|---|
| Left | `W` | `S` |
| Right | `Up arrow` | `Down arrow` |

## How it is built

```
Main.py                  game loop, input binding, scoring
components/
├── Paddle.py            paddle position and movement
├── Ball.py              velocity, wall bounce, paddle bounce, speed-up
└── Scoreboard.py        per-player score rendering
```

The ball reverses its y-velocity on a wall hit and its x-velocity on a paddle
hit, gaining a little speed each rally so points get harder to hold.

## Requirements

Python 3.10+. `turtle` is part of the standard library.
