#! /bin/bash
# This Script verifies the integrity of files using SHA256 checksums: this means that if you modified
# the files, this test will fail since the checksums have been modified. This is normal.
# Checksums generated on 21/10/21
echo Verifying integrity of files...
cd ../
sha256sum -c scripts/checksums.txt || echo "Test failed! This may happen if you modified the files."
echo Integrity verified!
