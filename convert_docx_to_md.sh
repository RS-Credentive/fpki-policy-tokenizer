for file in original_docx/*.docx
do
    # Two rounds of substitution since you can only apply it once per line
    originaldoc=${file#original_docx\/}
    filename=${originaldoc%.docx}
    echo converting $file
    pandoc-3.1.11/bin/pandoc $file -o "converted_markdown/$filename.md" --wrap=none --to=gfm-raw_html
done