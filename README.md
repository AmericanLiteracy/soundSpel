# soundSpel
SoundSpell word list for translation between traditional spelling and the soundSpell simplified spelling system.

Columns are:
1. **TS**: traditional spelling
1. **soundSpel**: soundSpel translation
1. **note**: Single character note abbreviation
    - \* asterisk denotes more attention is needed
    - 1 explicit exception
1. **alt**: alternative soundSpel versions under consideration
1. **Brit**: British pronounciation
1. **mult TS**: multiple entries of traditional spelling in column 1, e.g. homographs
1. **mult SS**: multiple entries of soundSpel in column 2, e.g. homophones
1. **long note**: any additional notes

How to convert dictionary from spreadsheet:
1. Start at https://docs.google.com/spreadsheets/d/1MxcI4qIKu0fh4yI4yIUTYOT2hAzSIebgC1pWfGhR-Bg/edit#gid=1708553670
1. File, download, csv
1. dos2unix soundSpelWurdList.csv
1. copy to spellingTranslator/master/dictionaries/soundSpel
1. cd /Users/mpeterse/repos/spellingTranslator/master
1. python tools/pickleDictionary.py
1. Now dictionaries/soundSpel.pickle is updated.
