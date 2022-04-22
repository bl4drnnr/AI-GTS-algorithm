# AI-GTS-algorithm

### Description

Prototype of GTS AI generating rules algorithm.

### Status
08.04.2022

- Generating only one rule.

09.04.2022

- Basic working prototype.

10.04.2022

- Done.

22.04.2022

- Rule evaluation parameters.

### Example of working

Al you need to do is just put your JSON data in `inputdata` in `input.json` file.

There is only **one** condition for the correct operation of the algorithm.

- Decision parameter needs to be placed on last place of every input record in `JSON`.

As a result you will get the table, that is going to look like this one,
where on the left side you can see index of the records and on the right side, after `-` symbol
you can see generated rule for this record. For example, you see in `input.json` you will see
this outcome.

PS: Duplicate index records mean that this records dedicates to 1+ rule.

---
```
1 - IF Lzawienie = normalne AND Astygmatyzm = nie THEN SOCZEWKI = miekkie
2 - IF Wiek = mlody AND Lzawienie = normalne AND Astygmatyzm = tak THEN SOCZEWKI = twarde
3 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
4 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
5 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
6 - IF Lzawienie = normalne AND Astygmatyzm = nie THEN SOCZEWKI = miekkie
7 - IF Wiek = mlody AND Lzawienie = normalne AND Astygmatyzm = tak THEN SOCZEWKI = twarde
7 - IF Wada_wzroku = krotkowidz AND Lzawienie = normalne AND Astygmatyzm = tak THEN SOCZEWKI = twarde
8 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
8 - IF Wiek = starczy AND Astygmatyzm = tak AND Wada_wzroku = dalekowidz THEN SOCZEWKI = brak
9 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
10 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
10 - IF Wiek = prestarczy AND Astygmatyzm = tak AND Wada_wzroku = dalekowidz THEN SOCZEWKI = brak
11 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
12 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
13 - IF Wada_wzroku = krotkowidz AND Lzawienie = normalne AND Astygmatyzm = tak THEN SOCZEWKI = twarde
14 - IF Lzawienie = normalne AND Astygmatyzm = nie THEN SOCZEWKI = miekkie
15 - IF Wiek = starczy AND Astygmatyzm = tak AND Wada_wzroku = dalekowidz THEN SOCZEWKI = brak
16 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
17 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
18 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
19 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
20 - IF Lzawienie = normalne AND Astygmatyzm = nie THEN SOCZEWKI = miekkie
21 - IF Lzawienie = normalne AND Astygmatyzm = nie THEN SOCZEWKI = miekkie
22 - IF Wiek = prestarczy AND Astygmatyzm = tak AND Wada_wzroku = dalekowidz THEN SOCZEWKI = brak
----------------------------------
LIST OF ALL RULES AND DEDICATED RECORDS TO THOSE RULES
1 - IF Lzawienie = normalne AND Astygmatyzm = nie THEN SOCZEWKI = miekkie - [1, 6, 14, 20, 21]
Rule's strength: 5
Rule's accuracy: 1.000
Rule's generality: 0.227
Rule's specificity: 1.000
Rule's support: 0.227
----------------
2 - IF Wiek = mlody AND Lzawienie = normalne AND Astygmatyzm = tak THEN SOCZEWKI = twarde - [2, 7]
Rule's strength: 2
Rule's accuracy: 1.000
Rule's generality: 0.091
Rule's specificity: 0.667
Rule's support: 0.091
----------------
3 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak - [3, 4, 5, 8, 9, 10, 11, 12, 16, 17, 18, 19]
Rule's strength: 12
Rule's accuracy: 1.000
Rule's generality: 0.545
Rule's specificity: 0.857
Rule's support: 0.545
----------------
4 - IF Wada_wzroku = krotkowidz AND Lzawienie = normalne AND Astygmatyzm = tak THEN SOCZEWKI = twarde - [7, 13]
Rule's strength: 2
Rule's accuracy: 1.000
Rule's generality: 0.091
Rule's specificity: 0.667
Rule's support: 0.091
----------------
5 - IF Wiek = starczy AND Astygmatyzm = tak AND Wada_wzroku = dalekowidz THEN SOCZEWKI = brak - [8, 15]
Rule's strength: 2
Rule's accuracy: 1.000
Rule's generality: 0.091
Rule's specificity: 0.143
Rule's support: 0.091
----------------
6 - IF Wiek = prestarczy AND Astygmatyzm = tak AND Wada_wzroku = dalekowidz THEN SOCZEWKI = brak - [10, 22]
Rule's strength: 2
Rule's accuracy: 1.000
Rule's generality: 0.091
Rule's specificity: 0.143
Rule's support: 0.091
----------------
```
