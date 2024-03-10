"""
Transform an SVG file by wrapping all <rect> and <path> elements in <a> tags.
"""

import os
from xml.etree.ElementTree import ElementTree, fromstring, tostring


def transform_svg(input_file: str, output_file: str):
    """
    Read an SVG file and transform it by wrapping all <rect> and <path> elements
    in <a> tags. The resulting SVG is written to the output file.

    :param input_file: The input SVG file path
    :param output_file: The output SVG file path
    """
    # Read the SVG content from the input file
    with open(input_file, mode="r", encoding="utf-8") as file:
        svg_1 = file.read()

    # Parse the original SVG content
    tree = ElementTree(fromstring(svg_1))
    root = tree.getroot()

    # Iterate over the SVG elements in reverse order
    prev_elements = []

    # Iterate over the SVG elements
    for elem in root:
        if elem.tag.endswith("a"):
            elem.set("target", "_blank")
            # Process the last two elements from prev_elements if they are 'rect' or 'path'
            for prev in prev_elements[-1:-3:-1]:
                if prev.tag.endswith(("rect", "path")):
                    elem.insert(0, prev)
                    # root.remove(prev)
        # Keep track of current element as a previous element for the next iteration
        prev_elements.append(elem)

    # Convert the modified XML tree back to a string and write to the output file
    tree.write(output_file, encoding="unicode", method="xml")


if __name__ == "__main__":
    input_file = os.path.join(".", "Roadmap.svg")
    output_file = os.path.join(".", "Roadmap-vf.svg")
    transform_svg(input_file, output_file)
    print(f"Modified SVG is written to {output_file}")
