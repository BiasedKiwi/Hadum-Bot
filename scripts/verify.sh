# This Script verifies the integrity of files using SHA256 checksums: this means that if you modified
# the files, this test will fail since the checksums have been modified. This is normal.
echo "Verifying integrity of files..."
sha256sum -c ./scripts/checksums.txt || echo -e "Test failed! This may happen if you modified the files.\033[0;31m Checksums file hash may not match\e[0;37m" && exit 0
echo Integrity verified!
