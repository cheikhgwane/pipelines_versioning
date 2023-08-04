from openhexa.sdk import current_run, pipeline, workspace, parameter
import pandas as pd


@pipeline("simple-etl", name="Simple ETL")
@parameter("initial", type=int, choices=[2, 5, 10], default=2)
def simple_etl(initial):
    count = task_1(initial)
    task_2(count)


@simple_etl.task
def task_1(initial):
    current_run.log_info("In task 1...")

    return initial + 42


@simple_etl.task
def task_2(count):
    current_run.log_info(f"In task 2... count is {count}")

    df = pd.DataFrame({"foo": [count]})
    output_path = f"{workspace.files_path}/count.csv"
    df.to_csv(output_path)
    current_run.add_file_output(output_path)


if __name__ == "__main__":
    simple_etl()
