## Preamble

This module is an optimized implementation of Ukkonen's suffix tree algorithm in python. In a near future it's going to have the most important text processing functionalities like:

### Search for strings:
  - Check if a string {\displaystyle P} P of length {\displaystyle m} m is a substring in {\displaystyle O(m)} O(m) time.[4]  
  - Find the first occurrence of the patterns {\displaystyle P_{1},\dots ,P_{q}} P_1,\dots,P_q of total length {\displaystyle m} m as substrings in {\displaystyle O(m)} O(m) time.
  - Find all {\displaystyle z} z occurrences of the patterns {\displaystyle P_{1},\dots ,P_{q}} P_1,\dots,P_q of total length {\displaystyle m} m as substrings in {\displaystyle O(m+z)} O(m+z) time.[5]
  - Search for a regular expression P in time expected sublinear in {\displaystyle n} n.[6]
  - Find for each suffix of a pattern {\displaystyle P} P, the length of the longest match between a prefix of {\displaystyle P[i\dots m]} P[i\dots m] and a substring in {\displaystyle D} D in {\displaystyle \Theta (m)} \Theta(m) time.[7] This is termed the matching statistics for {\displaystyle P} P.
 
### Find properties of the strings:
  - Find the longest common substrings of the string {\displaystyle S_{i}} S_{i} and {\displaystyle S_{j}} S_j in {\displaystyle \Theta (n_{i}+n_{j})} \Theta(n_i + n_j) time.[8]
  - Find all maximal pairs, maximal repeats or supermaximal repeats in {\displaystyle \Theta (n+z)} \Theta(n + z) time.[9]
  - Find the Lempel–Ziv decomposition in {\displaystyle \Theta (n)} \Theta (n) time.[10]
  - Find the longest repeated substrings in {\displaystyle \Theta (n)} \Theta (n) time.
  - Find the most frequently occurring substrings of a minimum length in {\displaystyle \Theta (n)} \Theta (n) time.
  - Find the shortest strings from {\displaystyle \Sigma } \Sigma  that do not occur in {\displaystyle D} D, in {\displaystyle O(n+z)} O(n + z) time, if there are {\displaystyle z} z such strings.
  - Find the shortest substrings occurring only once in {\displaystyle \Theta (n)} \Theta (n) time.
  - Find, for each {\displaystyle i} i, the shortest substrings of {\displaystyle S_{i}} S_{i} not occurring elsewhere in {\displaystyle D} D in {\displaystyle \Theta (n)} \Theta (n) time.

## Sourses:

  - http://web.stanford.edu/~mjkay/gusfield.pdf
  - On–line construction of suffix trees. Esko Ukkonen
  - http://www.geeksforgeeks.org/ukkonens-suffix-tree-construction-part-6/ 
