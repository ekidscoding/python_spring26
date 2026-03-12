# Installation Guide

[install uv](https://docs.astral.sh/uv/getting-started/installation/)

```shell
uv sync
```

## Cowsay 'Hello World!'

This uses [pypi.org/cowsay/](https://pypi.org/project/cowsay/)

```shell
uvx cowsay -t 'hello world!' -c "stegosaurus"
```

### Lessons List

#### 14 March 2026 - Функції

```
├── README.md
├── assets
│   └── img
│       └── pycallgraph.png
├── main.py
├── pyproject.toml
├── src
│   ├── params_callable.py
│   ├── params_callable_untyped.py
│   └── params_string.py
└── uv.lock
```

```shell
uv run src/params_callable.py
```

![`params_callable.py` Call Tree](assets/img/pycallgraph.png)

Generated with

```shell
pycallgraph -e '*lock*' -e '_find*' -e '_ModuleLock*' -e 'cb' --max-depth 4 graphviz --output-file=./assets/img/pycallgraph.png -- ./src/params_callable.py
```
