# Rapidly-Exploring Random Trees in Python
## Introduction
The rapidly-exploring random trees (RRT) algorithm is a probabilistic method of searching a space. At a high level, given a starting point (the root node of your tree), a map of your space, and an goal point, the RRT algorithm is as follows:

<pre>
Given starting point <b>s</b>, ending point <b>e</b>, map space <b>M</b>, undirected graph <b>T</b>
Add <b>s</b> as the root node of <b>T</b>
While no path <b>s</b>-><b>e</b> exists in <b>T</b>
    Choose a point <b>x</b> at random from <b>M</b>
    Try to draw an edge to the nearest node in <b>T</b>
    If success:
        Add <b>x</b> to the <b>T</b>
    Else:
        Discard <b>x</b>
    If <b>x</b> within some threshold distance from <b>e</b>:
        Attempt to add an edge <b>x</b>-><b>e</b>
        If success:
            Finished
</pre>

## Walkthrough

![Step 0](/doc/img/RRT_example_0.png)
![Step 1](/doc/img/RRT_example_1.png)
![Step 2](/doc/img/RRT_example_2.png)
![Step 3](/doc/img/RRT_example_3.png)
![Step 4](/doc/img/RRT_example_4.png)
![Step 5](/doc/img/RRT_example_5.png)
![Step 6](/doc/img/RRT_example_6.png)
![Step 7](/doc/img/RRT_example_7.png)