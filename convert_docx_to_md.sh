for file in original_docx/*.docx
do
    # Two rounds of substitution since you can only apply it once per line
    originaldoc=${file#original_docx\/}
    filename=${originaldoc%.docx}
    echo converting $file
    pandoc $file -o "converted_markdown/$filename.md" --wrap=none --atx-headers --grid_tables --to=markdown-simple_tables-pipe_tables-multiline_tables
done