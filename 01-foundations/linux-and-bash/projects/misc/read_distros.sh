#!/bin/bash

while read distro version release; do

	echo -e "Distro: $distro\tVersion $version\tReleased $release"

done < distros.txt

