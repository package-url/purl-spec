import pypandoc
import sys
import os
import re
import json
import shutil

# Example usage:
# [Repository Directory]/.venv/bin/python [Repository Directory]/aiu-sdk-website-fork/conversionScript/preprocessing.py aiu-sdk-website-fork/data/PURL.rst

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/..'

DOCS_DIR = ROOT_DIR + '/website/docs'
print('==============================' + DOCS_DIR)
SIDEBAR_PATH = ROOT_DIR + '/website/sidebars.js'

########################

def convert_md_to_docs(input_file):

    """
    Converts a .md docs file to a file hierarchy in the docs folder, corresponding to
    different sections in the documentation.

    TODO : Add error handling
    """

    input_file = input_file.replace('.rst', '.md')
    if not os.path.isfile(input_file):
        print(f"Error: '{input_file}' does not exist.")
        return
    
    with open(input_file, 'r') as f:
        f_lines = f.readlines()

    md_contents = ''
    out_md_path = ''

    for line in f_lines:
        if line.startswith('#'):

            if len(md_contents) > 0:
                with open(out_md_path, 'w') as f:
                    print(out_md_path)
                    f.write(md_contents)
                md_contents = ''

            md_section_name = line.replace('#','').strip()
            md_section_name = ''.join(char for char in md_section_name.replace(' ','_') if char.isalnum() or char == '_')

            os.makedirs(DOCS_DIR + '/' + md_section_name)

            out_md_path = DOCS_DIR + '/' + md_section_name + '/' + md_section_name + '.md'
        else:
            md_contents += line

    # for rootdir, _, filenames in os.walk(DOCS_DIR):
    #     if 

########################

def convert_rst_to_md(input_file, output_file=None):
    """
    Converts the input .rst file to a .md file. This is an intermediary step
    to process the input file for ease of use.
    """

    # Clear the docs directory if it is populated.
    if os.path.isdir(DOCS_DIR) and len(os.listdir(DOCS_DIR)) != 0:
        shutil.rmtree(DOCS_DIR)
    if not os.path.exists(DOCS_DIR):
        os.mkdir(DOCS_DIR)

    if not os.path.isfile(input_file):
        print(f"Error: '{input_file}' does not exist.")
        return

    output_file = os.path.splitext(input_file)[0] + ".md"

    try:
        # Convert rst to markdown
        output = pypandoc.convert_file(input_file, 'md', format='rst')

        # Replace angle-bracket links <https://example.com> with markdown links [https://example.com](https://example.com)
        output = re.sub(
            r'<(https?://[^ >]+)>',
            lambda m: f"[{m.group(1)}]({m.group(1)})",
            output
        )

        # Wrap {key: value} like objects in backticks to avoid MDX parsing errors
        # This regex matches {...} with some content inside
        output = re.sub(
            r'(\{[^}]+\})',
            r'`\1`',
            output
        )

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"Conversion complete: '{output_file}'")
    except Exception as e:
        print(f"Conversion failed: {e}")

########################

def docs_to_sidebar():
    """
    Generates a sidebar JSON file from the docs folder. The output will be fed into the
    sidebars.js file.
    """

    res = []
    for rootdir, _, filenames in os.walk(DOCS_DIR):

        # Do not consider empty directories.
        if len(filenames) == 0 and rootdir != DOCS_DIR:
            print(' N H H ', rootdir)
            os.rmdir(rootdir)
            continue

        rootdir = ''.join(rootdir.split('docs')[1:])[1:]

        elem = {
            "type" : "category",
            "label" : rootdir,
            "items" : [
                {
                    "type" : "doc",
                    "label" : filename.split('.')[0],
                    "id" : os.path.join(rootdir, filename)[:-3]
                } for filename in filenames
            ]
        }
        res.append(elem)

    res.pop(0) # Pop the top-level docs directory as it is not necessary
    res = json.dumps(res, indent=1)

    return res

########################

def generate_sidebar():

    sidebar = docs_to_sidebar()
    with open(SIDEBAR_PATH, 'w') as f:
        f.write('''
        /** @type {import(\'@docusaurus/plugin-content-docs\').SidebarsConfig} */
        const sidebars = {
        mySidebar : ''' + sidebar +
        '}; export default sidebars;')

    

########################

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert_rst_to_md.py <input.rst>")
    else:
        convert_rst_to_md(sys.argv[1])
        convert_md_to_docs(sys.argv[1])
        generate_sidebar()