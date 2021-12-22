import sys, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

GLYPHS_FILE_IN = "./FiraCode.glyphs"
GLYPHS_FILE_OUT = "./FiraMod.glyphs"
if len(sys.argv) > 1:
    GLYPHS_FILE_OUT = sys.argv[1]


glyphs_content = open(GLYPHS_FILE_IN, "r").read()

# # glyphs_content = glyphs_content.replace('familyName = "Fira Code";', 'familyName = "Fira Mod";')

## I really want to disable all the contextual alternates, but leaving the code entry blank
##   or removing this section entirely makes the compilation fail. I don't understand the
##   file format well enough to be more surgical about this, so I'm setting up a single dummy
##   subsitution rule that has no actual effect.
glyphs_lines = glyphs_content.splitlines()
calt_idx = glyphs_lines.index("name = calt;")
glyphs_lines[calt_idx-1] = 'code = "sub zero by zero;";'

with open(GLYPHS_FILE_OUT, "w") as outfile:
    outfile.write("\n".join(glyphs_lines))


