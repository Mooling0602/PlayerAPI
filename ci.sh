#!/bin/bash
./pack_and_doc.sh
if [ $? -ne 0 ]; then
    echo "pack_and_doc.sh failed"
    exit 1
fi
cp docs_auto.md docs/full/en_us.md
echo "Auto updated docs fully in en_us."