from pathlib import Path

from dagster_dbt import DbtProject

dbt_project_2 = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..", "dbt_project_2").resolve(),
    packaged_project_dir=Path(__file__).joinpath("..", "..", "dbt-project-2").resolve(),
)
dbt_project_2.prepare_if_dev()
