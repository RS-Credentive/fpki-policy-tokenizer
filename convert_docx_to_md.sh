for file in original_docx/*.docx
do
    # Two rounds of substitution since you can only apply it once per line
    originaldoc=${file#original_docx\/}
    filename=${originaldoc%.docx}
    pandoc $file -o "converted_markdown/$filename.md" --wrap=none
done