# Rapidly-Exploring Random Trees in Python
## Introduction
The rapidly-exploring random trees (RRT) algorithm is a probabilistic method of searching a space. At a high level, given a starting point (the root node of your tree), a map of your space, and an goal point, the RRT algorithm is as follows:


>Given starting point **s**, ending point **e**, map space **M**, undirected graph **T**
>Add **s** as the root node of **T**
>While no path **s**->**e** exists in **T**
>    Choose a point **x** at random from **M**
>    Try to draw an edge to the nearest node in **T**
>    If success:
>        Add **x** to the **T**
>    Else:
>        Discard **x**
>    If **x** within some threshold distance from **e**:
>        Attempt to add an edge **x** -> **e**
>        If success:
>            Finished

