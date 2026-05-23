"""Convert a text string into a single SVG path (no <text> elements).

Reads a TTF, lays out the requested text at the right size, and emits SVG
path data so the rendered name has no literal text in the markup — only
coordinate data.

Run from the website root:
    /home/shoroy/miniconda3/envs/website/bin/python scripts/text-to-svg-path.py

Writes assets/hero-name.svg and prints the inline-ready snippet.
"""

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

TEXT = "Shobhan Roy"
FONT_PATH = "/usr/share/fonts/truetype/lato/Lato-Bold.ttf"
OUTPUT_SVG = "assets/hero-name.svg"

# Target visual size matches the website's hero H1. The H1 uses
# font-size: clamp(1.9rem, 3vw, 2.8rem). We render at a nominal upem
# scale and let CSS scale the SVG to match the H1 height. The viewBox
# height is set from the font's ascent/descent at the nominal size.
NOMINAL_FONT_SIZE_PX = 60  # nominal — the SVG scales via CSS height clamp

font = TTFont(FONT_PATH)
glyph_set = font.getGlyphSet()
cmap = font.getBestCmap()
units_per_em = font["head"].unitsPerEm
hhea = font["hhea"]
ascent = hhea.ascent
descent = hhea.descent  # negative

scale = NOMINAL_FONT_SIZE_PX / units_per_em

pen = SVGPathPen(glyph_set)
x_cursor = 0
for ch in TEXT:
    if ch == " ":
        # use the advance width of a space glyph
        space_glyph = cmap.get(ord(" "), None)
        if space_glyph is None:
            x_cursor += int(units_per_em * 0.25)
        else:
            x_cursor += glyph_set[space_glyph].width
        continue
    glyph_name = cmap.get(ord(ch))
    if glyph_name is None:
        continue
    glyph = glyph_set[glyph_name]
    # SVGPathPen accumulates everything into one path. We need to offset
    # each glyph horizontally; use a transformed pen via the pen protocol.
    pen.moveTo  # touch — we'll instead use a transform via cu copy
    # Simpler: serialize a temp pen per glyph and translate the path data
    from fontTools.pens.transformPen import TransformPen
    tpen = TransformPen(pen, (1, 0, 0, 1, x_cursor, 0))
    glyph.draw(tpen)
    x_cursor += glyph.width

# Compute width / viewBox in font units, then scale to nominal px
width_units = x_cursor
height_units = ascent - descent  # ascent positive, descent negative

width_px = width_units * scale
height_px = height_units * scale

# SVG uses y-down; fontTools paths come in font coords (y-up). Apply a
# vertical flip so the glyphs render upright. Translate by ascent so the
# baseline lands correctly.
path_d = pen.getCommands()

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width_units} {height_units}" role="img" aria-label="Site header">
  <g transform="translate(0,{ascent}) scale(1,-1)">
    <path d="{path_d}" fill="currentColor"/>
  </g>
</svg>
"""

with open(OUTPUT_SVG, "w") as f:
    f.write(svg)

print(f"Wrote {OUTPUT_SVG}")
print(f"  viewBox: 0 0 {width_units} {height_units}")
print(f"  nominal render: {width_px:.0f}x{height_px:.0f}px")
print(f"  aspect ratio: {width_units/height_units:.3f}")
