echo "Build project summary file..."
pandoc 00_project-summary.md --pdf-engine=xelatex -o project-summary.pdf
echo "...complete!"

echo "Build project description file..."
pandoc 01_project-description.md --pdf-engine=xelatex -o project-description.pdf
echo "...complete!"

echo "Build references file..."
pandoc 02_references.md --pdf-engine=xelatex -o references.pdf
echo "...complete!"

echo "Build budget justification file..."
pandoc 03_budget-justification.md --pdf-engine=xelatex -o budget-justification.pdf
echo "...complete!"

echo "Build facilities file..."
pandoc 04_facilities.md --pdf-engine=xelatex -o facilities.pdf
echo "...complete!"

echo "Build data management plan file..."
pandoc 05_data-management-plan.md --pdf-engine=xelatex -o data-management-plan.pdf
echo "...complete!"

echo "Build program officer concurrence email file..."
pandoc 06_program-officer-concurrence-email.md --pdf-engine=xelatex -o program-officer-concurrence-email.pdf
echo "...complete!"
