from pyhero.chart.parser import Parser

sample = """
[Song]
{
  Name = "Can't Wait"
  Artist = "CHON"
  Charter = "jsonV"
  Album = "Grow"
  Year = ", 2015"
  Offset = 0
  Resolution = 192
  Player2 = bass
  Difficulty = 2
  PreviewStart = 0
  PreviewEnd = 0
  Genre = "Math Rock"
  MediaType = "cd"
  MusicStream = "song.ogg"
}
[SyncTrack]
{
  0 = TS 1
  0 = B 336000
  192 = TS 4
  192 = B 132000
}
[Events]
{
  0 = E "section Intro"
  6240 = E "section Verse 1"
  6624 = E "phrase_start"
  6720 = E "lyric Trying"
  7392 = E "lyric to"
  7488 = E "lyric find"
  8448 = E "lyric you"
  8640 = E "lyric left"
  8832 = E "lyric me"
  9024 = E "lyric lost"
  9216 = E "phrase_end"
  9984 = E "phrase_start"
  10176 = E "lyric I"
  10368 = E "lyric just"
  10560 = E "lyric want"
  10752 = E "lyric you"
  10944 = E "lyric home"
  11328 = E "lyric now"
  11472 = E "phrase_end"
  12192 = E "phrase_start"
  12384 = E "lyric and"
  12480 = E "lyric though"
  13056 = E "lyric I'll"
  13248 = E "lyric see"
  13440 = E "lyric you"
  13632 = E "lyric a-"
  13824 = E "lyric gain"
  14400 = E "lyric but"
  14664 = E "phrase_start"
  15840 = E "phrase_start"
  16032 = E "lyric I"
  16080 = E "lyric can't"
  16320 = E "lyric wait"
  16416 = E "lyric for-"
  16704 = E "lyric ever"
  16920 = E "phrase_end"
  18528 = E "section Chorus"
  18816 = E "phrase_start"
  19008 = E "lyric I"
  19200 = E "lyric can't"
  19392 = E "lyric wait"
  19584 = E "phrase_end"
  19728 = E "phrase_start"
  19872 = E "lyric I"
  19968 = E "lyric can't"
  20160 = E "lyric wait"
  20280 = E "phrase_end"
  20448 = E "phrase_start"
  20640 = E "lyric I"
  20688 = E "lyric can't"
  20928 = E "lyric wait"
  21024 = E "lyric any-"
  21216 = E "lyric more"
  21696 = E "lyric baby!"
  21816 = E "phrase_end"
  21960 = E "phrase_start"
  22080 = E "lyric I"
  22224 = E "lyric can't"
  22464 = E "lyric wait"
  22608 = E "phrase_end"
  22848 = E "phrase_start"
  23040 = E "lyric I"
  23232 = E "lyric wait"
  23424 = E "phrase_end"
  23568 = E "phrase_start"
  23712 = E "lyric I"
  23760 = E "lyric can't"
  24000 = E "lyric wait"
  24096 = E "lyric any-"
  24288 = E "lyric more"
  24528 = E "phrase_end"
  24672 = E "section Solo"
  30816 = E "section Verse 2"
  31056 = E "phrase_start"
  31248 = E "lyric I"
  31296 = E "lyric wish"
  32064 = E "lyric you"
  33024 = E "lyric were"
  33216 = E "lyric still"
  33600 = E "lyric here"
  33864 = E "phrase_end"
  34632 = E "phrase_start"
  34752 = E "lyric not"
  34944 = E "lyric just"
  35136 = E "lyric on"
  35328 = E "lyric my"
  35520 = E "lyric mind"
  35832 = E "phrase_end"
  36624 = E "phrase_start"
  36960 = E "lyric and"
  37056 = E "lyric though"
  37728 = E "lyric I'll"
  37824 = E "lyric see"
  38016 = E "lyric you"
  38208 = E "lyric a-"
  38400 = E "lyric gain"
  38976 = E "lyric but"
  39336 = E "phrase_end"
  40320 = E "phrase_start"
  40608 = E "lyric I"
  40704 = E "lyric can't"
  40896 = E "lyric wait"
  41088 = E "lyric for-"
  41280 = E "lyric ever"
  41616 = E "phrase_end"
  43104 = E "section Bridge"
  61416 = E "phrase_start"
  61632 = E "lyric Ooooooh"
  64872 = E "phrase_end"
  65040 = E "phrase_start"
  65088 = E "lyric Ooooooh"
  67680 = E "section Outro"
  67704 = E "phrase_end"
  67920 = E "phrase_start"
  68160 = E "lyric Trying"
  68832 = E "lyric to"
  68928 = E "lyric find"
  69192 = E "phrase_end"
  69768 = E "phrase_start"
  69888 = E "lyric you"
  70080 = E "lyric left"
  70272 = E "lyric me"
  70464 = E "lyric lost"
  71040 = E "phrase_end"
  71448 = E "phrase_start"
  71616 = E "lyric I"
  71808 = E "lyric just"
  72000 = E "lyric want"
  72192 = E "lyric you"
  72384 = E "lyric home"
  72768 = E "lyric now"
  73272 = E "phrase_end"
}
[ExpertSingle]
{
  192 = N 0 630
  192 = N 1 618
  192 = N 2 606
  192 = N 4 600
  906 = N 1 666
  930 = N 2 618
  954 = N 3 204
"""


def test_chart_parser():
    p = Parser()
    p.read_string(sample)
    assert len(p.sections()) == 4
    assert p["Song"]["Name"][0] == '"Can\'t Wait"'
    assert len(p["SyncTrack"]["0"]) == 2
    assert p["Events"]["0"][0] == 'E "section Intro"'
    assert p["ExpertSingle"]["192"][0] == "N 0 630"
