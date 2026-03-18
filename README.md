## Formosan-Kucapungane

This repository contains data for processing and structuring the Kucapungane dataset into the **FormosanBank XML format**. The dataset includes Rukai (Wutai dialect) stories from the Haocha (好茶) tribe and is organized to assist in linguistic research and language preservation.

## Project Structure

* `Final_XML`: Directory containing the processed data structured into FormosanBank XML format.

## Usage

The XMLs were created from the PDF using EasyOCR followed by extensive hand correction.

1. **Run EasyOCR to extract text from screenshots**
```
python easyOCR.py 
```
This produces raw text from the scanned PDF pages.
Required lots of hand correction.

2. **Hand format XML according to FormosanBank standards**

The raw OCR output was manually structured into FormosanBank XML format, with each Rukai sentence placed in `<FORM>` tags and the corresponding Chinese translation placed in `<TRANSL>` tags.

3. **Hand correct and verify**

All of the following were manually checked and corrected:
* Original Rukai text in `<FORM>` tags
* Chinese translations in `<TRANSL>` tags
* XML formatting and structure
