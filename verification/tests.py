"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [3, 8, True],
            "answer": '''  a
 h b
g   c
 f d
  e''',
        },
        {
            "input": [3, 6, False],
            "answer": '''  a
 b *
c   *
 d f
  e''',
        },
        {
            "input": [4, 10, False],
            "answer": '''   a
  b *
 c   *
d     j
 e   i
  f h
   g''',
        },
        {
            "input": [5, 16, True],
            "answer": '''    a
   p b
  o   c
 n     d
m       e
 l     f
  k   g
   j h
    i''',
        },
        {
            "input": [5, 14, False],
            "answer": '''    a
   b *
  c   *
 d     n
e       m
 f     l
  g   k
   h j
    i''',
        },
    ],
    "Extra": [
        {
            "input": [4, 1, False],
            "answer": '''   a
  * *
 *   *
*     *
 *   *
  * *
   *''',
        },
        {
            "input": [4, 0, False],
            "answer": '''   *
  * *
 *   *
*     *
 *   *
  * *
   *''',
        },
        {
            "input": [4, 0, True],
            "answer": '''   *
  * *
 *   *
*     *
 *   *
  * *
   *''',
        },
        {
            "input": [2, 3, False],
            "answer": ''' a
b *
 c''',
        },
        {
            "input": [2, 3, True],
            "answer": ''' a
* b
 c''',
        },
        {
            "input": [10, 26, False],
            "answer": '''         a
        b *
       c   *
      d     *
     e       *
    f         *
   g           *
  h             *
 i               *
j                 *
 k               *
  l             z
   m           y
    n         x
     o       w
      p     v
       q   u
        r t
         s''',
        },
        {
            "input": [8, 26, True],
            "answer": '''       a
      * b
     *   c
    z     d
   y       e
  x         f
 w           g
v             h
 u           i
  t         j
   s       k
    r     l
     q   m
      p n
       o''',
        },
    ]
}
