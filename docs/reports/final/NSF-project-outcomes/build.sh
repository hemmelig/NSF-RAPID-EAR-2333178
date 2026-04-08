echo "Build Project Outcomes file..."
pandoc project-outcomes.md --pdf-engine=xelatex -o project-outcomes.pdf
echo "...complete!"
