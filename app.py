import streamlit as st

st.title("Kalkulator Sederhana")
inputan = st.number_input("Masukkan angka pertama!", 0)
inputandua = st.number_input("Masukkan angka kedua!", 1)

with st.container():
	col1, col2, col3, col4 = st.columns(4)
	with col1 :
		if st.button("Tambah"):
			hasil = inputan + inputandua
			st.success(f"Hasil: {hasil}")
	with col2 :
		if st.button("Kurang"):
			hasil = inputan - inputandua
			st.success(f"Hasil: {hasil}")
	with col3 :
		if st.button("Kali"):
			hasil = inputan * inputandua
			st.success(f"Hasil: {hasil}")
	with col4 :
		if st.button("Bagi"):
			if inputandua == 0:
				st.error("Tidak bisa dibagi nol!")
			else:
				hasil = inputan / inputandua
				st.success(f"Hasil: {hasil}")