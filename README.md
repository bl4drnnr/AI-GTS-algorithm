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

### Example of working

Al you need to do is just put your JSON data in `inputdata` in `input.json` file.

There is only **one** condition for the correct operation of the algorithm.

- Decision parameter needs to be placed on last place of every input record in `JSON`.

As a result you will get the table, that is going to look like this one,
where on the left side you can see index of the records and on the right side, after `-` symbol
you can see generated rule for this record. For example, you see in `input.json` you will see
this outcome:


1 - IF Wada_wzroku = krotkowidz AND Lzawienie = normalne AND Astygmatyzm = nie THEN SOCZEWKI = miekkie
\
2 - IF Wiek = mlody AND Lzawienie = normalne AND Astygmatyzm = tak THEN SOCZEWKI = twarde
\
3 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
\
4 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
\
5 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
\
6 - IF Wada_wzroku = krotkowidz AND Lzawienie = normalne AND Astygmatyzm = nie THEN SOCZEWKI = miekkie
\
7 - IF Wiek = mlody AND Lzawienie = normalne AND Astygmatyzm = tak THEN SOCZEWKI = twarde
\
8 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
\
9 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
\
10 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
\
11 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
\
12 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
\
13 - IF Wada_wzroku = krotkowidz AND Lzawienie = normalne AND Astygmatyzm = tak THEN SOCZEWKI = twarde
\
14 - IF Wada_wzroku = dalekowidz AND Lzawienie = normalne AND Astygmatyzm = nie THEN SOCZEWKI = miekkie
\
15 - IF Wiek = starczy AND Astygmatyzm = tak AND Wada_wzroku = dalekowidz THEN SOCZEWKI = brak
\
16 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
\
17 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
\
18 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
\
19 - IF Lzawienie = zmniejszone THEN SOCZEWKI = brak
\
20 - IF Wada_wzroku = dalekowidz AND Lzawienie = normalne AND Astygmatyzm = nie THEN SOCZEWKI = miekkie
\
21 - IF Wada_wzroku = dalekowidz AND Lzawienie = normalne AND Astygmatyzm = nie THEN SOCZEWKI = miekkie
\
22 - IF Wiek = prestarczy AND Astygmatyzm = tak AND Wada_wzroku = dalekowidz THEN SOCZEWKI = brak


