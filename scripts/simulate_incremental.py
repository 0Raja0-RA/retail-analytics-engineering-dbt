import duckdb
import subprocess
import os
import sys

def main():
    print("=" * 60)
    print("PRAKTIK 17 - SIMULASI DATA BARU PADA INCREMENTAL MODEL")
    print("=" * 60)

    con = duckdb.connect('analytics.duckdb')

    c_before = con.execute('SELECT COUNT(*) FROM raw.orders').fetchone()[0]
    print(f"1. Jumlah baris raw.orders SEBELUM insert: {c_before}")

    print("2. Menambahkan 50 transaksi baru dari data/orders_incremental.csv...")
    con.execute("INSERT INTO raw.orders SELECT * FROM read_csv_auto('data/orders_incremental.csv', header=true);")

    c_after = con.execute('SELECT COUNT(*) FROM raw.orders').fetchone()[0]
    print(f"3. Jumlah baris raw.orders SESUDAH insert : {c_after} (Expected: 550)")

    con.close()

    print("\n4. Menjalankan dbt run hanya untuk model fct_sales_incremental:")
    dbt_exe = os.path.abspath(r'.venv\Scripts\dbt.exe')
    res = subprocess.run([dbt_exe, 'run', '--select', 'fct_sales_incremental'], cwd='dbt_project', capture_output=True, text=True)
    print(res.stdout)

    # Verifikasi jumlah baris di fct_sales_incremental
    con2 = duckdb.connect('analytics.duckdb')
    fct_count = con2.execute('SELECT COUNT(*) FROM main.fct_sales_incremental').fetchone()[0]
    print(f"5. Jumlah baris fct_sales_incremental sekarang: {fct_count} (Expected: 550)")
    con2.close()

if __name__ == '__main__':
    main()
