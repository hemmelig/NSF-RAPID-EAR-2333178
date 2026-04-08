echo "Build 2025 Annual Report file..."
pandoc annual-report-2025.md --pdf-engine=xelatex -o annual-report-2025.pdf
echo "...complete!"

echo "Build 2025 Field Report file..."
pandoc field-summary-2025.md --pdf-engine=xelatex -o field-summary-2025.pdf
echo "...complete!"
