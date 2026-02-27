Math Engine
==
This is a mathematical engine that can solve different kinds of equations or unequations. Well, it can't now, but I am working on it.

Structure
--
I am writing this on python. Logic is separated between three classes: relation, expression and component. 

Hierarchy
--
- Top class is relation. It has left side and right side (both expressions) and relation between them (like = or < etc.)
- Then goes expression. It consists of components or other expressions separated by + or -
- Components are parts of expression that only contain multiplication or division.