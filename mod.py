import sys, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

GLYPHS_FILE_IN = "./FiraCode.glyphs"
GLYPHS_FILE_OUT = "./FiraMod.glyphs"
if len(sys.argv) > 1:
    GLYPHS_FILE_OUT = sys.argv[1]


glyphs_content = open(GLYPHS_FILE_IN, "r").read()

## Change the family name so it's clear that this is something different.
glyphs_content = glyphs_content.replace('familyName = "Fira Code";', 'familyName = "Fira Mod";')

## I really want to disable all the contextual alternates, but leaving the code entry blank
##   or removing this section entirely makes the compilation fail. I don't understand the
##   file format well enough to be more surgical about this, so I'm setting up a single dummy
##   subsitution rule that has no actual effect.
glyphs_lines = glyphs_content.splitlines()
calt_idx = glyphs_lines.index("name = calt;")
glyphs_lines[calt_idx-1] = 'code = "sub zero by zero;";'

## TODO: update the version number with the latest upstream tag?

## Filenames need to be updated in build scripts, too, since some of the
## tools name outputs based on family name.
scripts = ["build_ttf.sh", "build_variable.sh", "build_woff.sh", "build_woff2.sh", "build_docker.sh", "build.sh"]
for buildscript in scripts:
    script_content = open(f"./script/{buildscript}", "r").read()
    script_content = script_content.replace("Fira Code", "Fira Mod")
    script_content = script_content.replace("FiraCode", "FiraMod")
    script_file = open(f"./script/{buildscript}", "w")
    script_file.write(script_content)
    script_file.close()


with open(GLYPHS_FILE_OUT, "w") as outfile:
    outfile.write("\n".join(glyphs_lines))


