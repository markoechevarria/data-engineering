for f in $(ls *.json); do
    airflow roles import "$f"
done