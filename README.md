# What is this for?
Here to be used with peace of mind, in order to;
* Validate the given number to be sure that if it's a valid Turkish ID number (TC Kimlik No) or not
* Generate new and valid Turkish ID numbers as much as wanted
* Find your relatives' (including siblings) TC ID numbers according to that they're whether younger or older than you
* Guess the missing part *(rightmost two digits)* of a deficient TC ID number with 9 *(leftmost)* digits

\**TC Kimlik No = Turkish ID (Number) = TC ID number*

## Nedir? (Turkish)
Yerel ve uluslararası tüm projelerde kullanılabilmesi için İngilizce yazılmıştır. TC kimlik numaralarını doğrulamak veya algoritmik test odaklı çeşitli ihtiyaçlar nedeniyle geçerli TC kimlik numaraları oluşturmak için kullanılabilir. Bu ihtiyaçlardan bazıları:
* Merak
* Algoritmanın test edilmesi
* Çeşitli sorgulama veya yazım denetimi işlevleri için hazır bekletilmek üzere geçerli TC kimlik numaraları barındıran bir havuz oluşturulması
* TC kimlik numaraları arasındaki farkın gözetlenmesi


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

### To find relatives (including siblings):
If you want to find your relatives' TC ID numbers, you can use this command. You need to use `-r` parameter with the `-o` (`--older`) or `-y` (`--younger`), by giving a limit, then a sample TC ID number to get the relatives according to. You can combine `-r` and `-o` or `-y` parameters like `-or` or `-yr`.

For example, in order to find three younger relatives according to the TC ID number 12345678901, use:
```
python turkish_ids.py -yr 3 -s 12345678901
```

It could be written also like this so:
```
python turkish_ids.py -r 3 --younger -s 12345678901
```

or like this:
```
python turkish_ids.py --younger --relatives 3 --start-from 12345678901
```

It's your choice.

### To guess the missing part of a TC ID number with 9 leftmost digits:
```
python turkish_ids.py -f 123456789
```
or
```
python turkish_ids.py --guess 123456789
```


---

## Algorithm:
### (Rule 1) To find the tenth digit:
n10 = ((n1+n3+n5+n7+n9)\*7-(n2+n4+n6+n8)) mod 10

### (Rule 2) To find the eleventh digit:
n11 = (n1+n2+..+n10) mod 10

### To check a TC ID number to be sure it's valid or not:
1. Its first digit should be greater than 0.
2. Its length should be 11 digits.
3. Check the tenth digit (n10) with the rule 1.
4. Check the eleventh digit (n11) with the rule 2.

### To find the relatives:
Take the first 9 leftmost digits of the TC ID number, then split it into two pieces from the fifth digit (including the fifth digit).

#### If you want to get an older relative:
Then you should add 3 to the first part and subtract 1 from the second part. The last thing you should do is to guess the tenth and eleventh digits of the TC ID number according to the rule 1 and the rule 2.

#### If you want to get a younger relative:
Then you should subtract 3 from the first part and add 1 to the second part. The last thing you should do is to guess the tenth and eleventh digits of the TC ID number according to the rule 1 and the rule 2.


## Disclaimer:
Its some or all functions may or may not work for someone randomly, for newborns or for one who's younger than a person born or married after 2000s (It's my guess but logically it might be right. After all TC ID numbers had been distributed, it was easy to know that a couple with a few or one child(ren) will have their own TC ID numbers related to the each other's TC ID number according to the relatives algorithm).
