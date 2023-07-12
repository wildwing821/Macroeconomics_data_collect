## Introduction

This is a script for downloading census data from various sources. The script is written in Python and uses the `requests` library to download files from URLs. The downloaded files are saved in specified paths.

## Requirements

The script requires the following Python libraries to be installed:

- `json`
- `random`
- `hashlib`
- `pdb`
- `bs4`
- `time`
- `datetime`
- `os`
- `requests`
- `traceback`

Make sure you have these libraries installed before running the script.

## Usage

1. Import the required libraries:

```python
import json
import random
import hashlib
import pdb
import bs4
import time
import datetime
import os
import requests
import traceback
import file_url_list
```

2. Set the `my_header` variable with the desired HTTP headers for the requests. This header is used for the requests made in the script.

3. Define the `delay_job` function which adds a random delay between 1 and 5 seconds. This function can be used to introduce delays between downloading files.

4. Implement the `dl_record` function to record the download history. This function writes the download date and text to a file named "dl_record.txt".

5. Implement the `getSoup` function to fetch the HTML content from a URL using the specified headers. The function returns a BeautifulSoup object.

6. Implement the `save_newaqi` function to save the downloaded content to a file with the name specified by the `fn` variable. The content is written in binary mode.

7. Implement the `save_hashvalue` function to save the calculated hash value to a file named "hashvalue.txt".

8. Implement the `cal_hashvalue` function to calculate the hash value of the passed content. The function returns the hash value.

9. Set the `fn` variable to the desired file name format. In the provided code, it is set to the current date in the format "%Y%m%d".

10. Implement the `download_check` function to check if a file needs to be downloaded. This function downloads the file from the specified URL using the `requests` library and performs the necessary checks.

11. Iterate over the URLs and paths in `file_url_list.path` and `file_url_list.url`, and call the `download_check` function for each pair.

12. After downloading the files, introduce a delay using the `delay_job` function.

13. Use the `getSoup` function to fetch the HTML content from the `file_url_list.url_nyfed` URL and find all the `<a>` tags.

14. Iterate over the found links and check if they match the desired criteria. If a matching link is found, construct the download URL and call the `download_check` function.

15. Introduce a delay using the `delay_job` function.

16. Use the `getSoup` function to fetch the HTML content from the `file_url_list.url_adp` URL and find all the `<a>` tags.

17. Iterate over the found links and check if they match the desired criteria. If a matching link is found, construct the download URL and call the `download_check` function.

18. The script execution ends.

Please ensure that the `file_url_list` module is properly defined and contains the necessary URLs and paths for downloading the files.

Feel free to modify the code and adapt it to your specific requirements.
