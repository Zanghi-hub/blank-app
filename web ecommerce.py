import streamlit_authenticator as stauth

# Danh sách mật khẩu bạn muốn hash
passwords = ['abc123']  # Thay bằng mật khẩu thực tế của bạn

# Tạo đối tượng Hasher với danh sách mật khẩu
hasher = stauth.Hasher(passwords)

# Generate hash mật khẩu
hashed_passwords = hasher.generate()

# In ra kết quả
print(hashed_passwords)

