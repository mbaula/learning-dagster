import duckdb

# Connect to the DuckDB database
conn = duckdb.connect(database="data/staging/data.duckdb")

# Execute the query to count rows in the trips table
result = conn.execute("select count(*) from trips").fetchall()

# Print the result
print(result)
