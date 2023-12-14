from argparse import ArgumentParser
import os

def format_file(input_file):
    """Takes in an unformatted file and formats it for our dataset"""
    formatted_lines = []
    current_speaker = None

    for line in input_file.readlines():
        stripped_line = line.strip()

        # Skip any empty lines
        if not stripped_line:
            continue

        # Check if the line contains a colon, then grab the speaker
        if ':' in stripped_line:
            # Only split by the first colon found, hopefully there isn't others
            parts = stripped_line.split(':', 1)
            current_speaker = parts[0].strip()

            # Remove the club information in brackets if that exists for speakers
            if '(' or ')' in current_speaker:
                speaker_parts = current_speaker.split('(')
                current_speaker = speaker_parts[0].strip()

            rest_of_line = parts[1].strip()

            # If there's a current speaker, prepend the speaker tag to the line
            formatted_line = f"[{current_speaker}]: {rest_of_line}"
            formatted_lines.append(formatted_line)

        elif current_speaker:
            # If there's a current speaker, continue their dialogue
            formatted_line = f"[{current_speaker}]: {stripped_line}"
            formatted_lines.append(formatted_line)

    return formatted_lines

def save_file(formatted_lines, output_filename):
    """Saves the file; creates directories if they don't exist"""
    output_directory = os.path.dirname(output_filename)
    os.makedirs(output_directory, exist_ok=True)

    with open(output_filename, 'w') as output_file:
        output_file.write('\n'.join(formatted_lines))

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    with open(args.file, 'r') as f:
        formatted_lines = format_file(f)

    # Generate the output file path dynamically
    output_directory = os.path.join("Formatted", os.path.dirname(args.file)).replace("Unformatted/", "")
    output_filename = os.path.join(output_directory, f"{os.path.basename(args.file)}")

    save_file(formatted_lines, output_filename)

    print(f"File formatted and saved as {output_filename}")
