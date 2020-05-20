for f in *.ipynb; do
	if [[ $f == "gen_page.ipynb" ]]; then
		continue;
	fi;
	echo -e "\e[34mConverting $f to HTML.\e[32m";
	jupyter nbconvert --to html $f;
done;