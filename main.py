import parse_utils

GEMEENTE_TLDS = 'https://raw.githubusercontent.com/mercator-working-group/gemeente-social/master/seed_lists/ron_seeds.csv'

# Parse the TLD+1 level page seed list.
page_list = parse_utils.parse_web_csv(GEMEENTE_TLDS)

# empty dictionary to hold keyeg websites by TLD+1
per_gemeente_links = {}

# Iterate over websites
for i in page_list:
    per_gemeente_links[i] = parse_utils.get_one_depth_links(
        i
    )

# Write the dict to a JSON on disk
parse_utils.write_dict_as_json(
    per_gemeente_links, 'ron-political-parties-out-full.json'
)
