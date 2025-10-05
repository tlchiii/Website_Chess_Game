from flask import Flask, render_template, request, jsonify
import pyodbc

app = Flask(__name__)

# ---------- KẾT NỐI SQL SERVER ----------
def get_db_connection():
    server = 'DESKTOP-8M88ESB\SQLEXPRESS'  # ví dụ: localhost\SQLEXPRESS
    database = 'CoVuaDB'
    
    conn_str = f'''
    DRIVER={{ODBC Driver 17 for SQL Server}};
    SERVER={server};
    DATABASE={database};
    Trusted_Connection=yes;
    '''
    conn = pyodbc.connect(conn_str)
    return conn

# ---------- Routes HTML ----------
@app.route('/')
def admin():
    return render_template('admin.html')

@app.route('/accounts')
def accounts_page():
    return render_template('accounts.html')

@app.route('/matches')
def matches_page():
    return render_template('matches.html')

@app.route('/posts')
def posts_page():
    return render_template('posts.html')


# ================== API: Tài khoản ==================
@app.route('/api/accounts', methods=['GET'])
def get_accounts():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TaiKhoan")
    rows = cursor.fetchall()
    data = [dict(zip([column[0] for column in cursor.description], row)) for row in rows]
    conn.close()
    return jsonify(data)

@app.route('/api/accounts', methods=['POST'])
def add_account():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO TaiKhoan (tenTK, matKhau, email, diem, mauCo, trangThai, phanQuyen) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (data['tenTK'], data['matKhau'], data['email'], data['diem'], data['mauCo'], data['trangThai'], data['phanQuyen'])
    )
    conn.commit()
    conn.close()
    return jsonify({'status':'ok'})

@app.route('/api/accounts/<int:id>', methods=['PUT'])
def update_account(id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE TaiKhoan SET tenTK=?, matKhau=?, email=?, diem=?, mauCo=?, trangThai=?, phanQuyen=? WHERE maTK=?",
        (data['tenTK'], data['matKhau'], data['email'], data['diem'], data['mauCo'], data['trangThai'], data['phanQuyen'], id)
    )
    conn.commit()
    conn.close()
    return jsonify({'status':'updated'})

@app.route('/api/accounts/<int:id>', methods=['DELETE'])
def delete_account(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM TaiKhoan WHERE maTK=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({'status':'deleted'})


# ================== API: Trận đấu ==================
@app.route('/api/matches', methods=['GET'])
def get_matches():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TranDau")
    rows = cursor.fetchall()
    data = [dict(zip([column[0] for column in cursor.description], row)) for row in rows]
    conn.close()
    return jsonify(data)

@app.route('/api/matches', methods=['POST'])
def add_match():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO TranDau (maTK1, maTK2, ketThucTran) VALUES (?, ?, ?)",
        (data['maTK1'], data['maTK2'], data['ketThucTran'])
    )
    conn.commit()
    conn.close()
    return jsonify({'status':'ok'})

@app.route('/api/matches/<int:id>', methods=['PUT'])
def update_match(id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE TranDau SET maTK1=?, maTK2=?, ketThucTran=? WHERE maTD=?",
        (data['maTK1'], data['maTK2'], data['ketThucTran'], id)
    )
    conn.commit()
    conn.close()
    return jsonify({'status':'updated'})

@app.route('/api/matches/<int:id>', methods=['DELETE'])
def delete_match(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM TranDau WHERE maTD=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({'status':'deleted'})


# ================== API: Bài viết ==================
@app.route('/api/posts', methods=['GET'])
def get_posts():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM BaiViet")
    rows = cursor.fetchall()
    data = [dict(zip([column[0] for column in cursor.description], row)) for row in rows]
    conn.close()
    return jsonify(data)

@app.route('/api/posts', methods=['POST'])
def add_post():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO BaiViet (tieuDe, noiDung, maTK) VALUES (?, ?, ?)",
        (data['tieuDe'], data['noiDung'], data['maTK'])
    )
    conn.commit()
    conn.close()
    return jsonify({'status':'ok'})

@app.route('/api/posts/<int:id>', methods=['PUT'])
def update_post(id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE BaiViet SET tieuDe=?, noiDung=?, maTK=? WHERE maBV=?",
        (data['tieuDe'], data['noiDung'], data['maTK'], id)
    )
    conn.commit()
    conn.close()
    return jsonify({'status':'updated'})

@app.route('/api/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM BaiViet WHERE maBV=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({'status':'deleted'})


if __name__ == '__main__':
    app.run(debug=True)
