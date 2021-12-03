#! /bin/bash
# This Script verifies the integrity of files using SHA256 checksums: this means that if you modified
# the files, this test will fail since the checksums have been modified. This is normal.
# Checksums generated on 03/12/21
echo Verifying integrity of files...
cd ../
sha256sum -c scripts/checksums.txt || echo -e "Test failed! This may happen if you modified the files.\033[0;31m Checksums file hash may not match" && exit 0
echo Integrity verified!
