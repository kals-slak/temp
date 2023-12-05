CREATE_TASK_TABLE = """
CREATE TABLE IF NOT EXISTS task_tables(
    task_id SERIAL PRIMARY KEY,
    task_name VARCHAR(50),
    end_date DATE,
    status INTEGER
);
"""

INSERT_TASK="INSERT INTO task_tables( task_name, end_date, status ) VALUES(%s, %s, %s)"
SELECT_ONE="SELECT * FROM task_tables WHERE task_id=%s"
SELECT_ALL_TASKS="SELECT * FROM task_tables"
SELECT_COMPLETED="SELECT * FROM task_tables WHERE status=0"
SELECT_IN_PROGRESS="SELECT * FROM task_tables WHERE status=1"
SELECT_FUTURE_TASKS="SELECT * FROM task_tables WHERE status=2"
SELECT_SORTED="""
SELECT * FROM task_tables
ORDER BY status, task_id
"""
SELECT_DEADLINE_TASK="SELECT * FROM task_tables WHERE end_date < %s AND status != 0"
SELECT_BY_DATE="SELECT * FROM task_tables WHERE end_date BETWEEN %s AND %s"
DELETE_ONE="DELETE FROM task_tables WHERE task_id=%s"

DROP_TABLE="DROP TABLE IF EXISTS task_tables"
