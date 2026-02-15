if database in batch_database:
    num_batches = math.ceil(len(sql_lines) / BATCH_SIZE)
    for i in range(num_batches):
        batch = sql_lines[i * BATCH_SIZE:(i + 1) * BATCH_SIZE]
        batch_sql = "\nUNION\n".join(batch)
        output_file = os.path.join(output_folder, f"{safe_dbname}_batch_{i+1}.sql")
        with open(output_file, "w") as f:
            f.write(batch_sql)
        print(f"Written {output_file} with {len(batch)} tables")