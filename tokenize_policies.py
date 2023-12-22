import stanza
import glob
import pathlib
import re

nlp = stanza.Pipeline('en', download_method=stanza.DownloadMethod.REUSE_RESOURCES)

def get_sentences(input: str) -> list[str]:
    sentences: list[str] = []
    processed_text: stanza.Document = nlp(input)
    for sentence in processed_text.sentences:
        sentences.append(sentence.text)
    return sentences


for markdown_doc in glob.glob("converted_markdown/minimal_test.md"):
    # Calculate the target filename from the source filename
    target_doc = pathlib.Path.joinpath(pathlib.Path.cwd(), pathlib.Path("tokenized_markdown"), pathlib.Path(markdown_doc).name)

    # open and tokenize the source file
    with open(markdown_doc) as raw_doc:
        policy_lines = raw_doc.readlines()

    line_count = len(policy_lines)

    # Precompile some regex we'll be using repeatedly
    # first, the regex for a markdown link
    md_link_re = re.compile(r"\[(?P<link>.*?)\]\((?P<target>.*?)\)(?P<text>.*)")

    processed_lines: list[str] = []
    for index, line in enumerate(policy_lines):
        print(f"Processing line {index} of {line_count} from {markdown_doc}.")

        # Ignore section headers "#"
        if line[0] == "#":
            processed_lines.append(line)

        # Process lines starting with links "[" separately
        elif line[0] == "[":
            line_matches = md_link_re.match(line)
            if line_matches is not None:
                first_line = ""
                matched_elements = line_matches.groupdict()
                if matched_elements["link"] != "":
                    first_line += f"[{matched_elements['link']}]"
                if matched_elements["target"] != "":
                    first_line += f"({matched_elements['target']})"
                if matched_elements["text"] != "":
                    sentences = get_sentences(input=matched_elements["text"])
                    first_line += sentences[0]
                    processed_lines.append(first_line)
                    # Add the rest of the sentences immediately after
                    processed_lines.extend([sentence for sentence in sentences])     
            else:
                # This line starts with '[' but is not a link - just copy it like a regular line
                processed_lines.extend(get_sentences(input=line))
                
        # if the line looks like a table
        elif line[0] == "|":
            # split the line into columns
            columns = line.split("|")
            # for each column, split into sentences - reassemble with a sentance per line
            # takes advantage of the fact that MD counts a single \n as equivalent to a space.
            for column in columns:
                sentences = get_sentences(input=column)
                # split strips the separater, so we'll need to add it back at the beginning of the first sentence
                if len(sentences) > 0:
                    sentences[0] = "|" + sentences[0]
                    processed_lines.extend(sentences)
            # Add the terminating '|' a the end of the last column
            processed_lines[-1] = processed_lines[-1] + "|"

        # If we get here, we're probably dealing with a regular line of text 
        else:
            processed_lines.extend(get_sentences(input=line))

    # Write out the tokenized file
    target_doc.write_text("\n".join(processed_lines), encoding="utf-8")