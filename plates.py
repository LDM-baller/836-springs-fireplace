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
    "Pale oak floors · rope-wrapped ring chandelier · whitewashed brick fireplace · pale blue walls."),
 9:("Living room, looking west",
    "The view out is the evening deck and the western sky. Cream sectional, leather sling "
    "chairs, oak coffee table, whitewashed brick fireplace."),
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
 16:("Downstairs landing, bunkroom beyond",
    "Shiplap walls, round black-strap mirror, and the built-in bunks through the doorway."),
 17:("The bunkroom bath",
    "Downstairs, serving the bunkroom. Cast-iron trough sink with two wall-mount bridge "
    "faucets, shiplap, recessed medicine cabinet, marble mosaic floor."),
 18:("The stair to the second floor",
    "Up to the primary and guest bedrooms. Navy patterned runner · painted balustrade and "
    "square newel · natural oak treads."),
 19:("The primary bedroom",
    "Second floor. Pale blue walls · vaulted ceiling · four-unit window bank · black sash "
    "with white casing · floor registers."),
 20:("The guest bedroom",
    "Second floor. A recessed dormer over the bed, two-tone wall, navy and cream bedding, "
    "pleated table lamps."),
 21:("The primary bath",
    "Second floor. Carrara wall tile and marble mosaic floor · two rain heads · white-oak "
    "vanity · polished-nickel fittings."),
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
 ("Downstairs", "The media room, the bunkroom and its bath.", [15,16,17]),
 ("Upstairs", "The stair, the two bedrooms and the primary bath.", [18,19,20,21]),
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
#
# Attributions corrected 2026-08-28 by Lindsay, going through the album photograph
# by photograph. The correction that reorganised everything: **the building with the
# red door is the BARN**, not the dwelling. Most of what was filed as "the house"
# before that pass was the barn, which had already been converted to living space
# by the time these pictures were taken.
#
# Directions here are Lindsay's unless a caption says otherwise. Where she could not
# place something, the caption says so rather than guessing.

ALBUM = {
 1:"⭐ The key frame. Camera looking south/south-west toward the Pollock-Krasner house — a neighbouring roofline stands in the background at the left. The barn is at centre with its red door; the pool in the foreground sat on its north side and is under the bluestone now; the building at the right became the great room.",
 2:"The barn’s red door and brick steps, close up",
 3:"The barn from the east — camera standing out toward Accabonac Harbor, looking back west",
 4:"The barn from the field, with the building that became the great room running off to the right",
 5:"Looking east: the building at centre is the current front entrance; the range on the left was the garage, now the media room, mud room and laundry",
 6:"The covered walk — a breezeway between two separate buildings, the garage range on the right",
 7:"The barn boarded up, work starting",
 8:"Inside the barn at ground level, a wall of three six-over-six windows",
 9:"The barn loft — batten door and glazed door under the roof slope",
 10:"Inside the barn: hand-hewn beams and the stair up to the loft",
 11:"Inside the barn looking east toward Accabonac Harbor — the red door is at the left of frame",
 12:"Inside the barn looking west toward what is now the evening deck. The camera stands where the kitchen is today; this wall and stair came out",
 13:"The fireplace, before it was whitewashed — it faces south, toward the Pollock-Krasner house",
 14:"The same fireplace framed out, lumber stacked",
 15:"The carved cast-iron firebox, stored in the barn during the work",
 16:"The barn loft — wide-plank floors, a cast-iron stove, and new ductwork threaded along the ceiling",
 17:"Glazed doors and the barn’s red door",
 18:"Camera facing south toward the Pollock-Krasner house; the evening deck was later built off to the right",
 19:"The barn loft stripped to the frame, new windows set, insulation stacked",
 20:"New roof framing — rafters and collar ties, not the barn’s trusses",
 21:"Re-shingling from the scaffold, new cedar going over weathered grey",
 22:"The new brick chimney — the one standing beside the entry porch today",
 23:"The east elevation finished, camera looking west",
 24:"The barn’s vaulted ceiling, dark-stained and without tie rods — the kitchen ceiling today",
}

ERAS = [
 ("I", "A compound, not a house", "before the previous renovation",
  "Four separate buildings, strung roughly west to east across the lot. Furthest west, the volume that "
  "is now the <b>front entrance</b>, with the <b>garage</b> and its long screened range beside it. Then "
  "the building that became the <b>great room</b>. Furthest east, closest to the water, the timber-framed "
  "<b>barn</b> &mdash; already fitted out for living, with a red door, a boxed stair up to a loft and "
  "whitewashed plaster between hand-hewn beams. An <b>in-ground pool</b> sat against the barn&rsquo;s "
  "north side, and a brick breezeway under a lattice arch ran between two of the others. Everything "
  "grey, everything weathered.",
  [1, 5, 6], []),
 ("II", "The renovation before this one", "2003 or later",
  "A gut, and a joining-up. Floors came out to the joists, walls back to the hand-hewn frame, windows "
  "out. New concrete-block foundations went in on the wetland side, a second floor was framed, a tall "
  "brick chimney was built, and the whole thing was re-shingled. <b>The four separate buildings were "
  "pulled together into the single footprint the survey now draws.</b> <b>The date comes from a Marvin "
  "&lsquo;Integrity&rsquo; window sticker propped against the brickwork in one frame &mdash; that line "
  "launched in 2003, and it is the only hard date anywhere in the album.</b>",
  [7, 10, 22, 12, 16, 23], []),
 ("III", "This renovation", "photographed by Tim Williams",
  "The barn survived a second time and became the kitchen &mdash; the hand-hewn frame reworked as "
  "painted trusses with steel tie rods threaded through, and the internal wall and stair taken out to "
  "open it up. The brick chimney stayed and the fireplace was whitewashed. The garage became the media "
  "room, mud room and laundry. The evening deck went in at the front entrance, and the pool ground "
  "became bluestone terrace.",
  [24], [13, 6, 23]),
]

TRACE = [
 ("The barn", "Kept, gutted", "Kept, opened up",
  "The oldest thing on the property and the only structure to survive both renovations. It was already "
  "living space before either — whitewashed plaster between hand-hewn beams, a boxed stair to a loft. "
  "This renovation took out that wall and stair; the kitchen stands where the stair was."),
 ("The barn’s roof trusses", "Dark-stained, exposed", "Painted, steel rods added",
  "The clearest then-and-now pair in the album: same truss geometry, same small square gable window. "
  "The timbers were dark; they were painted out and the steel tie rods threaded through."),
 ("The red door", "The barn’s door, behind a glazed porch", "Gone",
  "It appears in four frames and is the easiest thing to track the barn by. Nothing in the current "
  "photographs shows it."),
 ("The great-room building", "A separate building east of the entrance", "The great room",
  "In the earliest frame it stands to the right of the barn as its own structure. It is the room with "
  "the whitewashed brick fireplace today."),
 ("The garage", "A long range under a screened porch", "Media room, mud room, laundry",
  "Separate from everything else, with a brick breezeway under a lattice arch running to its neighbour."),
 ("The buildings themselves", "Separate", "One footprint",
  "Four of them, running west to east: front entrance, garage range, great room, barn. The album shows "
  "them standing apart with a dirt drive between; then a covered breezeway linking two; the 2021 survey "
  "draws a single merged outline. Separate, then linked, then merged."),
 ("The brick chimney", "Built new", "Kept, fireplace whitewashed",
  "Not original — it goes up during the previous renovation. It is the chimney beside the entry porch "
  "today, and the firebox it serves faces south toward the Pollock-Krasner house."),
 ("The in-ground pool", "In use", "Under the terrace",
  "It sits right against the barn in the earliest frames and again behind the new foundation wall. "
  "The bluestone terrace covers that ground now, and the pool never appears on the 2021 survey."),
 ("Wide-plank floors, cast-iron firebox", "Salvaged", "Unclear",
  "Both were photographed as kept pieces, the firebox stored in the barn mid-job. Whether either is in "
  "the house now is not visible in the Tim Williams set."),
]

ZONES = [
 ("approach","Road &amp; approach",42.0,43.5,
  "Springs Fireplace Road runs along the west boundary and the driveway loops in to the motor court. "
  "The sunset side.", [], [3,4,1], "surveyed"),
 ("garage","The garage — now media room",60.0,38.0,
  "A long range under a screened porch, standing separate with a brick breezeway running to its "
  "neighbour. Media room, mud room and laundry today.",
  [6], [15], "confirmed by Lindsay"),
 ("entrance","Front entrance &amp; evening deck",63.0,56.0,
  "The westernmost of the four buildings. The evening deck was built in front of and around it, which "
  "is why it is the sunset side.",
  [5], [6,7], "confirmed by Lindsay"),
 ("greatroom","The great room",72.0,52.0,
  "Its own building once, standing between the entrance and the barn. It holds the whitewashed brick "
  "fireplace, which faces south toward the Pollock-Krasner house.",
  [13,14,18], [8,9], "confirmed by Lindsay"),
 ("barn","The barn",80.0,45.0,
  "The easternmost building and the oldest, closest to the water. Already living space before either "
  "renovation; the kitchen today. Faces east toward Accabonac Harbor, red door on the north side.",
  [1,2,3,4,7,8,9,10,11,12,15,16,17,19,24], [13,14], "position approximate"),
 ("house","The dwelling",75.0,72.0,
  "The block the survey labels <i>2 Story Frame Dwelling</i>. The second floor, the roof framing and the "
  "new brick chimney all belong to the previous renovation.",
  [20,21,22], [11], "surveyed"),
 ("east","East terrace — where the pool was",83.0,62.0,
  "<i>Brick Patio</i> on the survey. The pool stood against the barn&rsquo;s north side and wrapped this "
  "corner; bluestone covers that ground now, with the fire pit on it.",
  [23], [22,23], "confirmed by Lindsay"),
 ("wetland","The wetland edge",93.0,63.0,
  "The revegetation and non-disturbance buffer along the east line — 4,053 sq ft of switch grass, "
  "little bluestem and northern bayberry. Beyond it, Accabonac Harbor.", [], [], "surveyed"),
]

PAGES = [("", "Gallery"), ("history/", "Three renovations"), ("map/", "Site map")]
