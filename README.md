# Jupyter Stack Setup

Demo of [Jupyter Notebook](http://jupyter.org/) and [PySpark](http://spark.apache.org/docs/2.4.0/api/python/pyspark.html) with the [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/).

- The environment will be suited for learning and developing applications for Apache Spark, using the Python, Scala, and R programming languages.

- Jupyter Notebooks enables interactive, and collaborative data analytics with Julia, Scala, Python, R, and SQL. Other uses include data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

Main itens included in the Stack:
- [SciPy](https://www.scipy.org/) (Python-based mathematics, science, and engineering)
- [SciKit-learn](http://scikit-learn.org/stable/)
- [SciKit-image](http://scikit-image.org/)
- [Pandas](https://pandas.pydata.org/)
- [Numexpr](https://github.com/pydata/numexpr)
- [Matplotlib](https://matplotlib.org/)
- [R](https://www.r-project.org/) interpreter and base environment
- [TensorFlow](https://www.tensorflow.org/)
- [Apache Spark](https://spark.apache.org/)
- [Apache Toree](https://toree.apache.org/)


## Setup

1. `git clone` this project from GitHub
2. Initialize Docker Swarm: `docker swarm init`
3. Deploy Stack: `docker stack deploy -c stack.yml jupyter-stack`
4. Confirm Stack is running: `docker stack ps jupyter-stack`
5. Install package so Python can interect with PostgreSQL:
```
docker exec -it \
$(docker ps | grep _pyspark | awk '{print $NF}') \
pip install psycopg2-binary
  ```

## Access Jupyter UI
- Go to [http://localhost:8888/](http://localhost:8888/)
- For this demo use the password: `password`

## Running Python Scripts
Open Jupyter Terminal by clicking on New > Terminal
```shell
cd $HOME/work/scripts
python ./01_simple_script.py
python ./02_bakery_dataframes.py
$SPARK_HOME/bin/spark-submit 02_bakery_dataframes.py
```

Load PostgreSQL with some data
```shell
python ./03_load_sql.py
```

Open Adminer at [http://localhost:8080/](http://localhost:8080/) to access PostgreSQL

- System: `PostgreSQL`
- Server: `postgres`
- Username: `postgres`
- Password: `postgres1234`
- Database: `demo`

## Running Jupyter Notebooks
At the home screen click on `notebooks` folder

Open `01_pyspark_demo_notebook.ipynb` or `02_pyspark_demo_notebook.ipynb`

- To run a line of the notebook press Control + Enter

## Remove Stack
```
docker stack rm jupyter-stack
```


## Misc
https://www.kaggle.com/datasets