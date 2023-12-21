# fpki-policy-tokenizer
A configuration for tokenizing FPKI Policy documents for processing downstream

## Basic process
1. Convert source documents (docx) to markdown
2. Process markdown files, creating one sentance per line. This will preserve paragraphs when viewed as markdown, but will make it easier to detect and process changes between versions.


## Notes
As of 2023.12.21, v 1.22 of the policy was reconstructed from a blackline version of 1.23