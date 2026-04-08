echo "Build 2024 Annual Report file..."
pandoc annual-report-2024.md --pdf-engine=xelatex -o annual-report-2024.pdf
echo "...complete!"

echo "Build 2024 Field Report file..."
pandoc field-summary-2024.md --pdf-engine=xelatex -o field-summary-2024.pdf
echo "...complete!"
