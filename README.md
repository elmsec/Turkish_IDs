# What is this for?
Here to be used with peace of mind in order to validate the given number to be sure that if it's a valid Turkish ID number (TC Kimlik No) or not, or to generate new and valid Turkish ID numbers as much as wanted.

\**TC Kimlik No = Turkish ID (Number) = TC ID number*

## How to use this?
**Note:** `12345678901` is a placeholder for your possible TC ID number(s).

### To validate the given TC ID number:
```
python turkish_ids.py -v 12345678901
```
or
```
python turkish_ids.py --validate 12345678901
```

### To generate new TC ID numbers:
Let's say you want to generate 10 new TC ID numbers by starting from the TC ID number **12345678901**. So you can use the commands below:
```
python turkish_ids.py -g 10 -s 12345678901
```
or
```
python turkish_ids.py --generate 10 --start-from 12345678901
```
