import duckdb

def main():
    print("Membuka database DuckDB (analytics.duckdb)...")
    con = duckdb.connect('analytics.duckdb')

    # 1. Setup schema raw dan load data dari CSV
    print("\n[1] Menyiapkan Schema Raw dan Memuat Data CSV:")
    con.execute("CREATE SCHEMA IF NOT EXISTS raw;")
    con.execute("CREATE OR REPLACE TABLE raw.customers AS SELECT * FROM read_csv_auto('data/customers.csv', header=true);")
    con.execute("CREATE OR REPLACE TABLE raw.products AS SELECT * FROM read_csv_auto('data/products.csv', header=true);")
    con.execute("CREATE OR REPLACE TABLE raw.orders AS SELECT * FROM read_csv_auto('data/orders.csv', header=true);")
    con.execute("CREATE OR REPLACE TABLE raw.payments AS SELECT * FROM read_csv_auto('data/payments.csv', header=true);")

    # Verifikasi jumlah baris (Praktik 9)
    print("\n--- Verifikasi Jumlah Record raw schema (Praktik 9) ---")
    for tbl in ['customers', 'products', 'orders', 'payments']:
        cnt = con.execute(f"SELECT COUNT(*) FROM raw.{tbl}").fetchone()[0]
        print(f"COUNT(raw.{tbl}): {cnt} baris")

    # 2. Menjalankan Query Agregasi Praktik 2
    print("\n[2] Menjalankan Query Agregasi SQL Dasar (Praktik 2):")
    query_p2 = """
    SELECT
        customer_id,
        ROUND(SUM(quantity * unit_price), 2) AS total_sales,
        SUM(quantity) AS total_items,
        COUNT(order_id) AS total_orders
    FROM raw.orders
    GROUP BY customer_id
    ORDER BY total_sales DESC
    LIMIT 10;
    """
    res = con.execute(query_p2).fetchall()
    cols = [desc[0] for desc in con.description]
    print(f"{cols[0]:<15} | {cols[1]:<15} | {cols[2]:<15} | {cols[3]:<15}")
    print("-" * 65)
    for row in res:
        print(f"{row[0]:<15} | {row[1]:<15.2f} | {row[2]:<15} | {row[3]:<15}")

    con.close()
    print("\nEksekusi query berhasil selesai.")

if __name__ == "__main__":
    main()
