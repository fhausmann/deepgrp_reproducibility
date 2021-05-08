for filename in $*; do
  echo "${filename}" >>protocol_linux.txt
  /usr/bin/time -a -o protocol_linux.txt RepeatMasker/RepeatMasker \
    -lib $PWD/humrep.lib \
    -pa 10 \
    -frag 300000 \
    -no_is \
    ${filename}
done
