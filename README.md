# Plotting-in-the-Nth-dimension
A tool build on top of Pygame in order to plot complex datasets

![alt text](https://github.com/Nijaoui-Wassim/Plotting-in-the-Nth-dimension/blob/main/sample.gif?raw=true)

# Plotting in The Nth Dimension

Wassim Nijaoui#1

_Concordia University_

_Montreal, Canada_

[1nijaouiwassim1@yahoo.com](mailto:1nijaouiwassim1@yahoo.comu)

_Abstract_— **This paper discusses a new technique that can be used for visualizing high-dimensional datasets of n dimensions. It explores the possibilities and applications as well that could be achieved using it. The paper will also show how this technique compare to preexisting techniques.**

Even by increasing the number of dimensions, spotting the patterns remains simple. We can as well treat the points as vectors (eigenvectors) and we can add the vectors so we can visualize a final point that take in account all the other points.

TABLE I

Complexity of the representation

1.

| Complexity of high-dimensional datasets |
| --- |
| 1D to 3 D | 3D to ~20 D | +20D |
| Flexible and dynamic representation easy to understand.
You can change the angles and shift them with an eigenvalue. | All the angles are shifted.
You can see the relationship between axis, and it is fairly simple enough

 | Images for examples
The effect from 1 dimension to another is smaller however a pattern emerges just from plotting enough points |


INTRODUCTION

The idea behind the axis that we will use to plot our points and the relationship between the points is that we will apply a linear transformation to each axis. Therefore, we will rotate and scale each vector plotted by an eigenvalue. Thus, we can create any number of axis and finally we will connect them to the center. The result of any dataset of n columns will be a 2D or a 3D representation of the connections between them as well as points plotted representing the whole row.

1. Intuition

As mentioned in the introduction, the idea is applying different linear transformation to the axis and plot the points from the dataset accordingly.

1. _Axis__Layout_

As mentioned, a unique Linear Transformation is applied to each axis in order to rotate it with a unique angle such that the sum of all axis angles add up to 360 degrees. Each axis is also scaled by a different or common factor depending on its distance from the origin.

![](RackMultipart20210111-4-1g0nlg8_html_e2f7aee82151997f.png)

Fig. 1 A sample line graph using colors which contrast well both on screen

Using the same idea, we can plot any number of axis. The smaller the angle, the more space we have for new axis. Here are few examples:

![alt text](https://github.com/Nijaoui-Wassim/Plotting-in-the-Nth-dimension/blob/main/screenshots/random/m2.png?raw=true)

Fig. 2 A sample line graph using colors which contrast well both on screen

1. Evaluation

1.

To avoid confusion, we have to keep in mind that all the shapes and connections between points are shifted by an eigenvector.

![alt text](https://github.com/Nijaoui-Wassim/Plotting-in-the-Nth-dimension/blob/main/screenshots/random/twodpng.png?raw=true)

Fig 3 – the red and white wine datasets visualized using 2 columns

**MINST dataset:**


![alt text](https://github.com/Nijaoui-Wassim/Plotting-in-the-Nth-dimension/blob/main/screenshots/minstall/all.png?raw=true)

Fig 4 – MINST presentation using all axis (our technique)

We can see in figure 4 the resulting points of different pictures of number 1 to 9 and how the different numbers have a unique vector summation.

![alt text](https://github.com/Nijaoui-Wassim/Plotting-in-the-Nth-dimension/blob/main/screenshots/minstall/circular_pat.png?raw=true)

Fig 5 – MINST dataset presentation for all numbers

![alt text](https://github.com/Nijaoui-Wassim/Plotting-in-the-Nth-dimension/blob/main/screenshots/minstall/coreeectminst.png?raw=true)

![alt text](https://github.com/Nijaoui-Wassim/Plotting-in-the-Nth-dimension/blob/main/screenshots/minstall/minstt.png?raw=true)

Fig 6 – MINST dataset presentation for all numbers

**Red / White Wine dataset:**

![alt text](https://github.com/Nijaoui-Wassim/Plotting-in-the-Nth-dimension/blob/main/screenshots/wine/one.png?raw=true)

Fig 7 – Wine dataset interpretation

![alt text](https://github.com/Nijaoui-Wassim/Plotting-in-the-Nth-dimension/blob/main/screenshots/wine/labl.png?raw=true)

Fig 8 – Wine dataset interpretation

![alt text](https://github.com/Nijaoui-Wassim/Plotting-in-the-Nth-dimension/blob/main/screenshots/random/a.png?raw=true)

Fig 9 – Wine dataset interpretation

**IV. CONCLUSIONS**

This technique is similar to the parallel coordinates&#39; technique. However, it is different in the sense that it conserves the angles between the axis to plot the resulting vector between them for example.

**REFERENCES**

[1] R. Clarke, H. W. Ressom, A. Wang, J. Xuan, M. C. Liu, E. A. Gehan, and Y. Wang, &quot;The properties of high-dimensional data spaces: implications for exploring gene and protein expression data,&quot; Nature Reviews Cancer, vol. 8, no. 1, pp. 37–49, 2008.

[2] C. Turkay, P. Filzmoser, and H. Hauser, &quot;Brushing dimensionsa dual visual analysis model for high-dimensional data,&quot; IEEE Transactions on Visualization and Computer Graphics, vol. 17, no. 12, pp. 2591–2599, 2011.

[3] D. Engel, K. Greff, C. Garth, K. Bein, A. Wexler, B. Hamann, and H. Hagen, &quot;Visual steering and verification of mass spectrometry data factorization in air quality research,&quot; IEEE Transactions on Visualization and Computer Graphics, vol. 18, no. 12, pp. 2275–2284, 2012.

[4] D. Maljovec, B. Wang, V. Pascucci, P.-T. Bremer, and D. Mandelli, &quot;Analyzing dynamic probabilistic risk assessment data through topology-based clustering,&quot; in Proceedings of International Topical Meeting on Probabilistic Safety Assessment and Analysis, 2013.

[5] S. Gerber, P. Bremer, V. Pascucci, and R. Whitaker, &quot;Visual exploration of high dimensional scalar functions,&quot; IEEE Transactions on Visualization and Computer Graphics, vol. 16, no. 6, pp. 1271–1280, 2010.

[6] A. Inselberg, Parallel Coordinates : Visual Multidimensional Geometry and its Applications. Springer, 2009.

[7] J. Heinrich and D. Weiskopf, &quot;State of the art of parallel coordinates,&quot; STAR Proceedings of Eurographics, vol. 2013, pp. 95–116, 2013.

[8] E. Bertini, A. Tatu, and D. Keim, &quot;Quality metrics in highdimensional data visualization: an overview and systematization,&quot; IEEE Transactions on Visualization and Computer Graphics, vol. 17, no. 12, pp. 2203–2212, 2011.

[9] G. Ellis and A. Dix, &quot;A taxonomy of clutter reduction for information visualisation,&quot; IEEE Transactions on Visualization and Computer Graphics, vol. 13, no. 6, pp. 1216–1223, 2007.

[10] P. E. Hoffman and G. G. Grinstein, &quot;A survey of visualizations for high-dimensional data mining,&quot; Information visualization in data mining and knowledge discovery, pp. 47–82, 2002.

[11] D. A. Keim, &quot;Information visualization and visual data mining,&quot; IEEE Transactions on Visualization and Computer Graphics, vol. 8, no. 1, pp. 1–8, 2002.

[12] M. C. F. De Oliveira and H. Levkowitz, &quot;From visual data exploration to visual data mining: A survey,&quot; IEEE Transactions on Visualization and Computer Graphics, vol. 9, no. 3, pp. 378–394, 2003.

[13] A. Buja, D. Cook, and D. F. Swayne, &quot;Interactive highdimensional data visualization,&quot; Journal of Computational and Graphical Statistics, vol. 5, no. 1, pp. pp. 78–99, 1996.

[14] R. Burger and H. Hauser, &quot;Visualization of multi-variate scientific ¨ data,&quot; Eurographics State of the Art Reports, pp. 117–134, 2007.

[15] J. Kehrer and H. Hauser, &quot;Visualization and visual analysis of multifaceted scientific data: A survey,&quot; IEEE Transactions on Visualization and Computer Graphics, vol. 19, no. 3, pp. 495–513, 2013.

[16] P. C. Wong and R. D. Bergeron, &quot;30 years of multidimensional multivariate visualization.&quot; in Proceedings of Scientific Visualization, Overviews, Methodologies, and Techniques, 1994, pp. 3–33.

[17] W. W.-Y. Chan, &quot;A survey on multivariate data visualization,&quot; Department of Computer Science and Engineering. Hong Kong University of Science and Technology, vol. 8, no. 6, pp. 1–29, 2006.

[18] T. Munzner, Visualization Analysis and Design. CRC Press, 2014.

[19] S. K. Card, J. D. Mackinlay, and B. Shneiderman, Readings in information visualization: using vision to think. Morgan Kaufmann, 1999.

[20] S. Liu, D. Maljovec, B. Wang, P.-T. Bremer, and V. Pascucci., &quot;Visualizing high-dimensional data: Advances in the past decade,&quot; Eurographics Conference on Visualization State of The Art Report, 2015.

[21] I. Jolliffe, Principal component analysis. Wiley Online Library, 2005. [22] Y. Koren and L. Carmel, &quot;Visualization of labeled data using linear transformations,&quot; in IEEE Symposium on Information Visualization, 2003, pp. 121–128.

[23] J. B. Tenenbaum, V. De Silva, and J. C. Langford, &quot;A global geometric framework for nonlinear dimensionality reduction,&quot; Science, vol. 290, no. 5500, pp. 2319–2323, 2000.

[24] M. Williams and T. Munzner, &quot;Steerable, progressive multidimensional scaling,&quot; in IEEE Symposium on Information Visualization, 2004, pp. 57–64.

[25] F. Paulovich, C. Silva, and L. Nonato, &quot;Two-phase mapping for projecting massive data sets,&quot; IEEE Transactions on Visualization and Computer Graphics, vol. 16, no. 6, pp. 1281–1290, 2010.

[26] F. Paulovich, D. Eler, J. Poco, C. Botha, R. Minghim, and L. Nonato, &quot;Piece wise laplacian-based projection for interactive data exploration and organization,&quot; Computer Graphics Forum, vol. 30, no. 3, pp. 1091–1100, 2011.

[27] E. T. Brown, J. Liu, C. E. Brodley, and R. Chang, &quot;Dis-function: Learning distance functions interactively,&quot; in IEEE Conference on Visual Analytics Science and Technology, 2012, pp. 83–92.

[28] M. Gleicher, &quot;Explainers: Expert explorations with crafted projections,&quot; IEEE Transactions on Visualization and Computer Graphics, vol. 19, no. 12, pp. 2042–2051, 2013. 16

[29] B. Mokbel, W. Lueks, A. Gisbrecht, and B. Hammer, &quot;Visualizing the quality of dimensionality reduction,&quot; Neurocomputing, vol. 112, pp. 109–123, 2013.

[30] S. Liu, B. Wang, P.-T. Bremer, and V. Pascucci, &quot;Distortion-guided structure-driven interactive exploration of high-dimensional data,&quot; Computer Graphics Forum, vol. 33, no. 3, pp. 101–110, 2014.
