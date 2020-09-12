# MICS
automate MICS dataset download

TODO

- [x] Login and download 
- [ ] Port to an R package
- [ ] Checking file hash to ignore dowloading existing file


# Required libs

See `meta.py`, tested using python3

```bash
pip3 install bs4
pip3 install selenium
# and what libs you are still missing...
```

# Logging in

This will open a new browser window (Firefox in this case).

Use your username, password, pass the reCaptcha and click login (then make no more movement in the browser please).
If we run the whole script, the rest of the code will wait until MICS logged in successfully and automatically redirect to surveys site.

# Example outputs

Get download urls

```python
Processing page 1
Processing page 2
Processing page 3
Processing page 4
Processing page 5
Processing page 6
There are 222 file(s) detected.
The-Gambia-MICS6-Datasets.zip is already existed.
Skip downloading The-Gambia-MICS6-Datasets.zip
```
