import sys

GLYPHS_FILE_IN = "./FiraCode.glyphs"
GLYPHS_FILE_OUT = "./FiraMod.glyphs"
if len(sys.argv) > 1:
    GLYPHS_FILE_OUT = sys.argv[1]

##### Not actually doing anything, just testing the workflow

# glyphs_content = open(GLYPHS_FILE_IN, "r").read()

# # glyphs_content = glyphs_content.replace('familyName = "Fira Code";', 'familyName = "Fira Mod";')

# # glyphs_lines = glyphs_content.splitlines()
# # calt_idx = glyphs_lines.index("name = calt;")
# # glyphs_lines[calt_idx-1] = 'code = "";'

# with open(GLYPHS_FILE_OUT, "w") as outfile:
#     outfile.write("\n".join(glyphs_lines))


