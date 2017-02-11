## Preamble

This module is an optimized implementation of Ukkonen's suffix tree algorithm in python. In a near future it's going to have the most important text processing functionalities like:

### Search for strings:
  - Check if a string ***P*** of length ***m*** is a substring in ***O(m)*** time.  
  - Find the first occurrence of the patterns ***P1,... ,Pq*** of total length ***m*** as substrings in ***O(m)*** time.
  - Find all ***z*** occurrences of the patterns ***P1,... ,Pq*** of total length ***m*** as substrings in ***O(m+z)*** time.
  - Search for a regular expression P in time expected sublinear in ***n***
  - Find for each suffix of a pattern ***P*** the length of the longest match between a prefix of ***P[i... m]*** and a substring in ***D*** in ***\theta (m)*** time. This is termed the matching statistics for ***P***
 
### Find properties of the strings:
  - Find the longest common substrings of the string ***Si*** and ***Sj*** in ***\theta (ni+nj)*** time.
  - Find all maximal pairs, maximal repeats or supermaximal repeats in ***\theta (n+z)*** time.
  - Find the Lempel–Ziv decomposition in ***\theta (n)*** time.[10]
  - Find the longest repeated substrings in ***\theta (n)*** time.
  - Find the most frequently occurring substrings of a minimum length in ***\theta (n)*** time.
  - Find the shortest strings from ***\Sigma***  that do not occur in ***D*** in ***O(n+z)*** time, if there are ***z*** such strings.
  - Find the shortest substrings occurring only once in ***\theta (n)*** time.
  - Find, for each ***i*** the shortest substrings of ***Si*** not occurring elsewhere in ***D*** in ***\theta (n)*** time.

## Sourses:

  - http://web.stanford.edu/~mjkay/gusfield.pdf
  - On–line construction of suffix trees. Esko Ukkonen
  - http://www.geeksforgeeks.org/ukkonens-suffix-tree-construction-part-6/ 
