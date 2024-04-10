import streamlit as st
import pandas as pd
import re


def search_dataframe(df, keyword):
    # Lakukan pencarian pada kolom id, kata1, atau kata2
    mask = df.apply(
        lambda row: any(
            keyword.lower() in str(row[col]).lower()
            for col in ["id", "madura", "indonesia"]
        ),
        axis=1,
    )
    search_results = df[mask]
    return search_results


def main():
    st.title("Pencarian Data dalam DataFrame")
    test_data = pd.read_csv(
        "https://raw.githubusercontent.com/ThoriqFathu/skripsi/main/kamus.csv"
    )
    data = test_data[["id", "madura", "indonesia", "keterangan"]]

    df = pd.DataFrame(data)
    # Mengubah semua nilai dalam kolom1 menjadi tipe string (str)
    df["id"] = df["id"].astype("str")

    # Tampilkan dataframe
    st.header("DataFrame:")
    st.write(df)

    # Input kata kunci untuk pencarian
    keyword = st.text_input("Masukkan kata kunci pencarian:", "")

    if st.button("Cari"):
        if keyword:
            pola = re.compile(r"\^a")
            keyword = re.sub(pola, "â", keyword)
            pola = re.compile(r"\`e")
            keyword = re.sub(pola, "è", keyword)
            # Lakukan pencarian berdasarkan kata kunci
            search_results = search_dataframe(df, keyword)
            if search_results.empty:
                st.info("Tidak ditemukan hasil untuk kata kunci tersebut.")
            else:
                st.header(f"Hasil Pencarian: {keyword}")
                st.write(search_results)
        else:
            st.warning("Masukkan kata kunci untuk memulai pencarian.")


if __name__ == "__main__":
    main()
