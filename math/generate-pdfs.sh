#!/bin/sh

set -x # echo on

# NOTE: You must have `pandoc` installed.

pandoc --from=gfm --to=pdf -o Units.pdf Units.md
pandoc --from=gfm --to=pdf -o TOV.pdf TOV.md
pandoc --from=markdown --to=pdf -o EoS.pdf EoS.md

