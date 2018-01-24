#!/usr/bin/env bash

git checkout master

echo "Building and deploying the docs"

cd docs
make clean
make notebooks
make html
cd ..

# commit and push
git add -A
git commit -m "building and pushing docs"
git push origin master

# Switch branches
git checkout gh-pages
rm -rf *
touch .nojekyll
git checkout master docs/_build/html
mv ./docs/_build/html/* ./
rm -rf ./docs

git add -A
git commit -m "publish new docs"
git push origin gh-pages

# Switch back to docs
git checkout master
