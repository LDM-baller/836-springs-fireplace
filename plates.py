# -*- coding: utf-8 -*-
"""Single source of truth for the 836 plate set.
Captions corrected 2026-08-28 per Lindsay. Compass directions are used ONLY
where she confirmed them: the evening deck faces the sunset (west), the barn
and the terrace face east. Every other direction claim was removed.
"""

# no -> (title, caption)
PLATES = {
 1:("Aerial over the property",
    "The house in its clearing — motor court, lawn, and Accabonac Harbor beyond."),
 2:("Roof plan from overhead",
    "Cedar roof, gravel motor court, terrace, and the planted meadow along the edge."),
 3:("The front, from the motor court",
    "White cedar shingle · black windows · bluestone plank walk · pea-gravel court."),
 4:("The front, three-quarter view",
    "Shingle coursing, black casements, ornamental grasses and nepeta at the foundation."),
 5:("The tall window in the gable end",
    "The gable end is the triangular wall under the peak of the roof; the oak was left "
    "standing on its own rather than in a group. Steel-grid window, exterior sconce, "
    "steel lawn edging, gravel and bluestone."),
 6:("The entry",
    "Bluestone plank-and-gravel walk · brick chimney · black door · half-round gutters."),
 7:("The evening deck",
    "Named for what it is used for — this is the sunset side. Painted pergola, hanging "
    "swing, bluestone steps, planted urn."),
 8:("The great room, end to end",
    "Pale oak floors · rope-wrapped ring chandelier · stacked-stone fireplace · pale blue walls."),
 9:("Living room, looking west",
    "The view out is the evening deck and the western sky. Cream sectional, leather sling "
    "chairs, oak coffee table, stone fireplace surround."),
 10:("Sliders open to the deck",
    "The indoor–outdoor move: the slider pockets away and the oak floor reads straight through."),
 11:("Dining against the window wall",
    "Steel windows and French doors · oak table · linear multi-shade chandelier."),
 12:("Dining, seen past the island",
    "Marble island top in the foreground, the grounds beyond."),
 13:("The original barn — now the kitchen",
    "The oldest structure on the property, facing east, kept and converted rather than "
    "replaced. Painted trusses, exposed steel tie rods, tall steel window, navy island, "
    "white dome pendants."),
 14:("The barn kitchen, from the dining side",
    "Navy shaker island · marble slab counter and backsplash · stainless range and hood · "
    "polished-nickel bar pulls."),
 15:("The media room",
    "Downstairs. Glazed double doors off the hall, vertical beadboard, blue runner, oak floor."),
 16:("The stair",
    "Navy patterned runner · painted balustrade and square newel · natural oak treads."),
 17:("Downstairs landing, bunkroom beyond",
    "Shiplap walls, round black-strap mirror, and the built-in bunks through the doorway."),
 18:("Bedroom under the vault",
    "Pale blue walls · four-unit window bank · black sash with white casing · floor registers."),
 19:("Bedroom with a recessed dormer",
    "Two-tone wall, navy and cream bedding, pleated table lamps."),
 20:("Primary bath",
    "Carrara wall tile and marble mosaic floor · two rain heads · white-oak vanity · "
    "polished-nickel fittings."),
 21:("The bunkroom bath",
    "Downstairs, serving the bunkroom. Cast-iron trough sink with two wall-mount bridge "
    "faucets, shiplap, recessed medicine cabinet, marble mosaic floor."),
 22:("The east elevation and the sunroom wing",
    "The terrace side. Full rear massing, bluestone terrace, steel-and-glass wing at the end."),
 23:("The terrace in use",
    "Bluestone terrace and steps · teak dining · round gas fire pit · black Adirondacks."),
 24:("The east elevation from the lawn",
    "How the house sits down into the grade; shingle weathering evenly."),
 25:("The outbuilding across the terrace",
    "Matching shingle and roof · steel sliders · covered porch on the main house at right."),
}

SECTIONS = [
 ("The Site", "Two frames from the air — the only ones that show the property whole.", [1,2]),
 ("Approach &amp; the Evening Deck", "The motor court, the entry walk, and the deck they watch the sunset from.", [3,4,5,6,7]),
 ("Living", "The main room, and the wall that opens onto the evening deck.", [8,9,10]),
 ("The Barn", "The kitchen and dining room occupy the oldest structure on the property.", [11,12,13,14]),
 ("Downstairs", "Media room, stair, and the bunkroom landing.", [15,16,17]),
 ("Bedrooms &amp; Baths", "Two bedrooms, the primary bath, and the bunkroom bath downstairs.", [18,19,20,21]),
 ("The East Terrace", "The side the house looks out over, and where it is actually lived in.", [22,23,24,25]),
]

# Historical notes. All four verified: three from public record, the fourth from the
# owners' own deed chain (Lee Krasner's signature appears in the title history).
HISTORY = [
 ("V", "The neighbours at 830",
  "The Pollock-Krasner House and Study Center sits immediately up the road at 830 Springs "
  "Fireplace Road. Lee Krasner and Jackson Pollock bought the 1879 fisherman's house there in "
  "November 1945, with a $2,000 down payment lent by Peggy Guggenheim against future work. "
  "Pollock painted in an upstairs bedroom until 1946, when he had the barn moved to open up the "
  "view and began using it as a studio — the drip paintings, <em>Autumn Rhythm</em>, "
  "<em>Convergence</em> and <em>Blue Poles</em> among them, were made on its floor. He worked "
  "there until his death in 1956; Krasner used the same barn until hers in 1984. The property "
  "became a National Historic Landmark in 1994 and has been open as a museum since 1988."),
 ("V", "Accabonac Harbor",
  "The tidal harbor the property looks toward. Its salt marsh is among the least altered on "
  "eastern Long Island, which is why so much of the shoreline around it is under permanent "
  "protection rather than under houses."),
 ("V", "Merrill Lake Sanctuary",
  "Twenty-nine acres of sunlit salt marsh and oak hummock on the harbor, with the entrance on "
  "Springs Fireplace Road — one of the first preserves the Nature Conservancy's Long Island "
  "chapter ever took on. Osprey nest there; red fox, piping plover and least tern use it; sea "
  "lavender and marsh elder grow in it. A 1.3-mile trail runs out and back, dawn to dusk."),
 ("V", "836 was Pollock and Krasner land",
  "Confirmed by the owners from the deed chain: this property was part of the Pollock and Krasner "
  "holding, and Lee Krasner's signature appears on a deed in the title history. The barn that now "
  "contains the kitchen stands from that period. It is a different building from the studio barn "
  "at 830 — that one is the museum — but it is of the same place and the same years."),
]


# ---------------------------------------------------------------- album pages

# The renovation before this one, from the album Lindsay filmed. id -> caption.
ALBUM = {
 1:"The house with the old pool in front of it", 2:"The red door, white surround, brick steps",
 3:"The house from the west lawn", 4:"House and outbuildings seen from the field",
 5:"The shed range and outbuildings", 6:"The covered walk along the sheds",
 7:"Boarded up, work starting", 8:"Barn stripped back \u2014 twelve-light windows",
 9:"Barn interior, door and plywood", 10:"Hand-hewn beams and the old stair",
 11:"Whitewashed room under hand-hewn beams", 12:"The white stair with iron balusters",
 13:"Brick chimney breast exposed", 14:"Fireplace framed, lumber stacked",
 15:"The carved cast-iron firebox \u2014 kept", 16:"Wide-plank floors and the cast-iron stove \u2014 kept",
 17:"Glazed doors and the red door", 18:"Beadboard wainscot going in",
 19:"New framing, insulation stacked", 20:"Attic framing",
 21:"Re-shingling from the scaffold", 22:"The new brick chimney going up",
 23:"Rear elevation, new construction", 24:"Dark beams against the white ceiling",
}

# roman, title, subtitle, body, [(album id, caption override or None)], [plate ids]
ERAS = [
 ("I", "The compound", "before the previous renovation",
  "Not one house but a cluster: a two-storey shingled dwelling with a red door and brick steps, a "
  "timber-framed barn with a run of glazing set into its roof slope, a long low shed range under a "
  "covered walk, and an in-ground pool sitting right up against the house. Everything grey, "
  "everything weathered.",
  [1, 5, 2], [1]),
 ("II", "The renovation before this one", "from the album",
  "A gut. Floors came out to the joists, walls back to the hand-hewn frame, windows out. New "
  "concrete-block foundations went in on the wetland side, a second floor was framed onto the "
  "dwelling, a tall brick chimney was built, and the whole thing was re-shingled. The barn was kept. "
  "So were the wide-plank floors and a carved cast-iron firebox.",
  [7, 10, 22, 12, 16, 23], []),
 ("III", "This renovation", "photographed by Tim Williams",
  "The barn survived a second time and became the kitchen \u2014 the hand-hewn frame reworked as "
  "painted trusses with steel tie rods through it. The brick chimney stayed. The pool ground became "
  "the bluestone terrace and fire pit. Everything went white cedar, black steel windows, marble and oak.",
  [], [13, 6, 23]),
]

# element, then, now, evidence
TRACE = [
 ("The barn", "Kept", "Kept",
  "The oldest thing on the property and the only structure to survive both renovations intact. "
  "Pollock-and-Krasner-era. Now the kitchen."),
 ("The brick chimney", "Built new", "Kept",
  "Not original \u2014 it goes up in the album\u2019s photographs. It is the chimney beside the entry porch today."),
 ("The dwelling", "Gutted, second floor added", "Rebuilt around",
  "The core is old; the massing was largely set by the previous renovation, on new block foundations "
  "toward the wetland."),
 ("The in-ground pool", "Still in use", "Gone",
  "Visible beside the house in the album, and again behind the new foundation wall. Absent from every "
  "current frame, and absent from the 2021 survey \u2014 the terrace and fire pit occupy that ground."),
 ("The shed range", "Standing", "Possibly the outbuilding",
  "A long low range under a covered walk. Something of that footprint reads as the outbuilding across "
  "the terrace today, but this one is an inference."),
 ("Wide-plank floors, cast-iron firebox", "Salvaged", "Unclear",
  "Both were photographed as saved pieces. Whether either survived into the current house is not "
  "visible in the Tim Williams set."),
]

# key, label, x%, y%, blurb, album ids, plate ids, confidence
ZONES = [
 ("approach","Road &amp; approach",42.0,43.5,
  "Springs Fireplace Road runs along the west boundary; the driveway loops in to the motor court. "
  "This is the sunset side.", [3,4], [3,4,1], "surveyed"),
 ("house","The dwelling",75.0,68.0,
  "The survey labels this block <i>2 Story Frame Dwelling</i>. Its core is old, but the massing was "
  "largely set by the previous renovation \u2014 second floor added, new chimney, re-shingled.",
  [1,2,7,12,13,14,17,18,20,21,22], [8,9,11], "surveyed"),
 ("porch","The porch",64.5,55.0,
  "Labelled <i>Porch</i> on the west face of the dwelling. The entry side.", [], [6], "surveyed"),
 ("barn","The barn",70.0,40.0,
  "The oldest structure, and now the kitchen. <b>Its exact position inside the footprint is not "
  "labelled on the survey</b> \u2014 this marker sits at the north block, which is a reading of the "
  "photographs, not a surveyed fact.", [8,9,10,11,24], [13,14], "inferred"),
 ("sheds","Outbuildings &amp; shed range",57.0,60.0,
  "A long low range under a covered walk, standing before the previous renovation. Whether it became "
  "the outbuilding across the terrace, or was lost, is <b>not settled</b>.", [5,6], [25], "inferred"),
 ("east","East side \u2014 patio and terrace",81.0,53.0,
  "<i>Brick Patio</i> and <i>Existing Patio and Deck to be Replaced / Repaired in Place</i>. The pool "
  "sat somewhere on this side; the bluestone terrace and fire pit are here now.", [19,23], [22,23], "surveyed"),
 ("wetland","The wetland edge",93.0,63.0,
  "The revegetation and non-disturbance buffer along the east line \u2014 4,053 sq ft of switch grass, "
  "little bluestem and northern bayberry. Beyond it, Accabonac Harbor.", [], [], "surveyed"),
]

PAGES = [("", "Gallery"), ("history/", "Three renovations"), ("map/", "Site map")]
