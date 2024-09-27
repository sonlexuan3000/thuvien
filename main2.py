import requests

# URL của API check-in
url = "https://libcalendar.ntu.edu.sg/r/checkin"

# Payload: đây là dữ liệu bạn đã thu thập được từ Developer Tools
# Đảm bảo các tham số như 'code', 'user_id', 'session_id' có giá trị chính xác
payload = {
    "code": "7ah",  # Thay bằng mã check-in hợp lệ mà bạn đã kiểm tra
    # Thêm các trường khác nếu API yêu cầu (ví dụ: 'user_id', 'session_id')
}

# Headers: bao gồm thêm Referer và User-Agent
headers = {
    "Content-Type": "application/json",  # Đảm bảo định dạng là JSON
    "Referer": "https://libcalendar.ntu.edu.sg/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Gửi yêu cầu POST tới API
response = requests.post(url, json=payload, headers=headers)

# Kiểm tra phản hồi từ API để xem chi tiết lỗi
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")

# Nếu API trả về lỗi, in chi tiết
if response.status_code != 200:
    print(f"Lỗi {response.status_code}: {response.text}")
else:
    print("Check-in thành công!")
