#!/bin/bash
mcdreforged pack
echo "Generating documentation..."
pydoc-markdown -p player_api --render-toc > docs_auto.md
echo "Finished."