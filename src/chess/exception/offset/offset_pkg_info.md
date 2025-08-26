Offset__mul__() has: (a)Many edge cases and conditions that differ significantly from plain
Offset.(c)High cohesion among Offset scalar edge cases and conditions.
(c)Offset-scalar-multiplication is a separate concern from creating an offset.
4) For managing offset-scalar-multiplication I: (i) Placed multiplication exceptions in the 
5) same module.(ii) Wrote a separate unit test for offset-scalar-multiplication.
