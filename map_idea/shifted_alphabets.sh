#!/usr/bin/env bash

alphabet_list=({A..Z})

for ((i=0;i<26;i++)); do
	for ((j=0;j<26;j++)); do
		index=$(( (i+j) % 26 ))
		echo -n "${alphabet_list[index]} "
	done
	echo
done
