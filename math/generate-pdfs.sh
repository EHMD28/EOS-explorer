#!/bin/sh

# NOTE: You must have `pandoc` installed.

pandoc --from=gfm --to=pdf -o Units.pdf Units.md
pandoc --from=gfm --to=pdf -o TOV.pdf TOV.md
