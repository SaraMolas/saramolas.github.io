#!/bin/sh
# Start a local preview at http://localhost:4000 with live reload.
# Uses Homebrew's Ruby 3.3 (GitHub Pages doesn't support Ruby 4 yet).
set -e
cd "$(dirname "$0")"
export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"
bundle check >/dev/null 2>&1 || bundle install
exec bundle exec jekyll serve --livereload "$@"
