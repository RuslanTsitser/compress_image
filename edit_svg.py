import xml.etree.ElementTree as ET

def merge_similar_paths(svg_file):
    tree = ET.parse(svg_file)
    root = tree.getroot()

    # Dictionary to store paths by fill color
    paths_by_fill = {}

    # Iterate over all path elements in the SVG
    for path in root.findall('.//{http://www.w3.org/2000/svg}path'):
        fill_color = path.get('fill')

        # Group paths by fill color
        if fill_color in paths_by_fill:
            paths_by_fill[fill_color].append(path)
        else:
            paths_by_fill[fill_color] = [path]

    # Logic to merge paths with the same fill color
    # Note: This is a placeholder. Actual merging logic will depend on how you want to combine the paths
    for fill_color, paths in paths_by_fill.items():
        if len(paths) > 1:
            # Example: keep the first path, remove others
            for path in paths[1:]:
                root.remove(path)

    # Save the modified SVG
    tree.write('merged_output.svg')

# Example usage
merge_similar_paths('/Users/ruslantsitser/dev/projects/sandbox/compress_image/old_svg/space_human.svg')
