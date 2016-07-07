# Batch Extract EAD3 to CSV

This extractor pulls out the contents of `<titleproper>`, `<scopecontent>` (all paragraphs), and children of `<origination>` and puts them into a CSV under `dc:title`, `dc:description`, and `dc:creator`. Multiple variables are separated by `|` and multiple paragraphs in `<scopecontent>` are separated by unicode line breaks. Quotation marks are replaced by unicode quotation marks in order to allow each section to be wrapped in quotation marks for safety. Much of this handling has to do with the specific needs of CurateND's batch ingester and the characters in Notre Dame's finding aids.

The extractor sets the filename, minus ".xml" as `dc:identifier`, which is being used for internal purposes. Similarly it creates a link to the Archives' website as `dc:source`.

The extractor adds hardcoded fields for `type`, `owner`, and `access` and the filename as `files`, all of which are specific to CurateND's batch ingester.

## To use

1. Edit variable `directory` (line 61) or turn it into a `raw_input` string and add to the end.
2. Edit appropriate lines in `createCSV` (line 72). Lines which should be considered have comments explaining the internal uses.
3. Make any decisions in line 11 re: the desired separator between `<part>` elements
4. Run `python process.py`
