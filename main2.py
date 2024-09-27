import requests

# URL của API check-in
url = "https://libcalendar.ntu.edu.sg/r/checkin"

# Payload: đây là dữ liệu bạn đã thu thập được từ Developer Tools
# Đảm bảo các tham số như 'code', 'user_id', 'session_id' có giá trị chính xác
payload = {
    "code": "D9JQ",  # Thay bằng mã check-in hợp lệ mà bạn đã kiểm tra
    # Thêm các trường khác nếu API yêu cầu (ví dụ: 'user_id', 'session_id')
}

# Headers: bao gồm thêm Referer và User-Agent
headers = {
    "Referer": "https://libcalendar.ntu.edu.sg/r/checkin",
}

# Gửi yêu cầu POST tới API
response = requests.post(url, data=payload, headers=headers)

# Kiểm tra phản hồi từ API để xem chi tiết lỗi
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")

# Nếu API trả về lỗi, in chi tiết
if response.status_code != 200:
    print("Error:", response.text, response.status_code)
else:
    print("Check-in thành công!")
