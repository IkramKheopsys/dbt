




from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
#from ..include.processing_script import hello, processing_spark
import subprocess
from airflow.operators.python_operator import PythonOperator
import os
import sys

# Ajouter le chemin du répertoire contenant les modules externes au sys.path
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'include'))
if module_path not in sys.path:
    sys.path.append(module_path)

# Maintenant, vous pouvez importer les modules externes normalement
#from processing_script import hello, processing_spark


# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 7),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}




def spark_processing():
# Créer une session Spark
   from pyspark.sql import SparkSession
   spark = SparkSession.builder \
    .appName("Traitement de données CSV avec Spark") \
    .getOrCreate()

# Charger les données CSV
  # csv_file_path = "~/my_postgres_db/seeds/data.csv"
   csv_file_path = os.path.expanduser('~/my_postgres_db/seeds/data.csv')
   df = spark.read.csv(csv_file_path, header=True, inferSchema=True)
   df.printSchema()
   df.show()
   filtered_df = df.filter(df["name"] == "value") 
   filtered_df.show() 
   spark.stop()





# Define the DAG
dag = DAG(
    'data_pipeline',
    default_args=default_args,
    description='Pipeline to process data with Spark and DBT',
    schedule_interval='@daily',
)



#Task to INIT dbt
run_pyspark= BashOperator(
    task_id='run_pyspark',
    bash_command='pip install pyspark',
    dag=dag,
)

spark_task = PythonOperator(
    task_id='spark_processing_task',
    python_callable=spark_processing,
    dag=dag
)


def run_dbt_init():
    command = "dbt init users"
    process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.stdin.write(b"1\n")  # Répondre à "Enter a number" avec "1"
    process.stdin.write(b"airflow\n")
    process.stdin.write(b"airflow\n")
    process.stdin.write(b"airflow\n")
    process.stdin.write(b"4\n")
    process.stdin.flush()
    output, error = process.communicate()
    print(output.decode())
    print(error.decode())


# Définir la fonction hello
def hello():
    print("Hello, world!")


hello_task = PythonOperator(
        task_id='hello',
        python_callable=hello,
        # provide_context=True
        dag=dag,
    )


# Define the tasks for each step of the pipeline
preprocessing_task = BashOperator(

    task_id='install_dbt',
    bash_command='pip install dbt-postgres',
    dag=dag,
)


#Task to INIT dbt
init_dbt_task = BashOperator(
    task_id='init_dbt',
    bash_command='dbt init users',
    dag=dag,
)



# Task to run dbt
debug_dbt_task = BashOperator(
    task_id='debug_dbt',
    bash_command='cd ~/my_postgres_db && dbt debug',
    dag=dag,
)


# Définition de la tâche PythonOperator pour exécuter dbt init





run_dbt_init_task = PythonOperator(
    task_id='run_dbt_init_task',
    python_callable=run_dbt_init,
    dag=dag,
)

# Task to run dbt

run_dbt_task = BashOperator(
    task_id='run_dbt',
    bash_command='cd ~/my_postgres_db && dbt run',
    dag=dag,
)




snapshot_dbt_task = BashOperator(
    task_id='snapshot_dbt',
    bash_command='cd ~/my_postgres_db && dbt snapshot',
    dag=dag,
)


# add install git 
hello_task >> run_pyspark  >> preprocessing_task >> run_dbt_init_task >> debug_dbt_task >> run_dbt_task >> snapshot_dbt_task
