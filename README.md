# saramolas.github.io

Personal research website, built with Jekyll and hosted on GitHub Pages.

## Where things live

| What | File |
| --- | --- |
| Homepage intro, news and project cards | `index.md` |
| Project cards (image, one-sentence summary, links) | `_data/projects.yml` |
| News items | `_data/news.yml` |
| Long-form project write-ups | `research.md` |
| Page template (header, nav, footer) | `_layouts/default.html` |
| Styles | `assets/css/main.css` |
| Site title, nav links, social links | `_config.yml` |

## Preview locally (macOS)

One-time setup: install Ruby 3.3 with [Homebrew](https://brew.sh). The macOS system
Ruby (2.6) is too old, and GitHub Pages doesn't support Ruby 4 yet.

```sh
brew install ruby@3.3
```

Start the local server with live reload (installs the gems into `vendor/bundle` on first run):

```sh
./serve.sh
```

Then open <http://localhost:4000>. Pages reload automatically when you save a file
(changes to `_config.yml` need a server restart).
