# geospatial-data-project


## 1. Requirements --> possible resource

First step: I will make a first filter according to the requirements and I will see how can I get the corresponding information.


1. Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design. 

    - Companies collection to be filtered throgh Mongo.

2. 30% of the company have at least 1 child.

    - To be searched through an API: kindergartens.

3. Developers like to be near successful tech startups that have raised at least 1 Million dollars.

    - Companies collection to be filtered throgh Mongo.

4. Executives like Starbucks A LOT. Ensure there's a starbucks not to far.

    - To be searched through google API: Starbucks.

5. Account managers need to travel a lot.

    - The offices needs to be not too far from an airport.

6. All people in the company have between 25 and 40 years, give them some place to go to party.

    - A young population country (to be checked throgh an API or an existing dataset)
    - And the party places near by.

7. The CEO is Vegan.

    - I will check the nearest vegan food place around the already decided office just to suck up the CEO. But this is not going to be a mandatory requirement for my decision.

8. If you want to make the maintenance guy happy, a basketball stadium must be around 10 Km.

    - To be searched through google API: bascketball staium . This is much more important  than the CEO desire.

9. The office dog "Pepe" needs a hairdresser every month. Ensure there's one not too far away.

    - I will check the nearest dog hairdresser place around the already decided office. But this is not going to be a mandatory requirement for my decision.


## 2. Companies collection analysis

I will filter the companies following the points 1 and 3.

- Design companies
- Tech startups that have raised > 1 Million dollars.


## 3. Population research

I got a dataset from [Department of Finance of California](http://www.dof.ca.gov/Forecasting/Demographics/Projections/).
I loaded the dataset in tableau public where I had to clean and prepare the data before using it. Finally I could make a dynamic [population pyramid](https://public.tableau.com/profile/isabel.searle.riesgo#!/vizhome/CaliforniaPopulationPyramid/California?publish=yes) where I could filter by county and see the evolution during the years. 




https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/los-angeles.geojson



## Mistakes and waste of time:

- Starting the analysis from a wrong side: making population pyramides of the whole word. [population pyramid](https://public.tableau.com/profile/isabel.searle.riesgo#!/vizhome/PopulationPyramid_16053098713460/PopulationPyramid?publish=yes), data from [The World Bank](https://data.worldbank.org/indicator/SP.POP.TOTL).

    - Solution: schematize step by step before starting to use the tools.

- Filtering without using $unwind: I spent too much time cleaning the dataframe.

     - Solution: read the class notes before starting to use the tools.

- MongoDB: trying to create the field "coor" following the class notes  step by step but not taking into account that I had teminated my iterator.

    - Solution: make a better debuging.

- Forgetting to import libraries in the funtions file. 

    - Solution: make a better debuging.

- Calling the response of the queries with the same name.

    - Solution: no commments...


