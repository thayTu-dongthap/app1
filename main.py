import tkinter as tk
import speedtest
from threading import Thread
def measure_speed():
    try:
        # Nút bắt đầu ẩn xuống, hiển thị "Đang đo..."
        _btn.config(state='disabled', text='Đang đo...')
        # Khởi tạo đối tượng trong thư viện speedtest
        st = speedtest.Speedtest()
        # Thông tin máy chủ
        st.get_best_server()
        # tính và đổi đơn vị sang mb
        download = st.download() / 1_000_000  # Convert to Mbps
        upload = st.upload() / 1_000_000  # Convert to Mbps
        ping = st.results.ping
        # Cập nhật thông tin sau khi chạy chương trình
        lbl_download.config(text=f"{download:.2f} Mbps")
        lbl_upload.config(text=f"{upload:.2f} Mbps")
        lbl_ping.config(text=f"{ping:.0f} ms")
    except Exception as ex:
        # Hiển thị lỗi
        tk.Label(window, text=f"Lỗi: {print(ex)}", font=title_font).pack(pady=10)
        lbl_download.config(text="Lỗi kết nối")
        lbl_upload.config(text="Kiểm tra mạng")
        lbl_ping.config(text="---")
    finally:
        _btn.config(state='normal', text='Bắt đầu đo')
def start_test():
    # Run speed test in separate thread
    Thread(target=measure_speed).start()
# Khowir tạo window form
window = tk.Tk()
window.title("Kểm tra tốc độ internet")
window.geometry("400x350")

# Chọn font chữ, cỡ chữ, kiểu chữ cho các đối tượng hiển thị thông tin
title_font = ('Times New Roman', 14, 'bold')
label_font = ('Times New Roman', 12)
result_font = ('Times New Roman', 12, 'bold')

# Tạo tiêu đề hiển thị thông tin ứng dụng
tk.Label(window, text="KIỂM TRA TỐC ĐỘ INTERNET", font=title_font).pack(pady=10)

# Hiển thị tốc độ tải xuống
tk.Label(window, text="Tốc độ tải xuống: ", font=label_font).pack()
lbl_download = tk.Label(window, text="0.00 Mbps", font=result_font, fg='red')
lbl_download.pack(pady=5)

# Hiển thị thông tin tốc độ tải lên
tk.Label(window, text="Tốc độ tải lên: ", font=label_font).pack()
lbl_upload = tk.Label(window, text="0.00 Mbps", font=result_font, fg='red')
lbl_upload.pack(pady=5)

# Hiển thị thông tin độ trễ
tk.Label(window, text="Độ trễ (Ping): ", font=label_font).pack()
lbl_ping = tk.Label(window, text="0 ms", font=result_font, fg='red')
lbl_ping.pack(pady=5)

# Tạo nút Bắt đầu đo khi click vào chạy hàm start_test
_btn = tk.Button(window, text="Bắt đầu đo", command=start_test, font=label_font)
_btn.pack(pady=10)
# Start GUI
window.mainloop()