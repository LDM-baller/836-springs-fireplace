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
