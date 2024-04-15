rand_num=$((RANDOM % 26))

rand_let=$(echo $((rand_num + 97)) | awk '{printf "%c", $1}')

echo $rand_let >> file.txt

git add .
git commit -m "chure${rand_num}"
git push -u origin main

