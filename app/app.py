from flask import Flask, request, render_template_string
import sqlite3
import os

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    cursor.execute("INSERT OR IGNORE INTO users (id, username, email) VALUES (1, 'admin', 'admin@example.com')")
    cursor.execute("INSERT OR IGNORE INTO users (id, username, email) VALUES (2, 'user', 'user@example.com')")
    conn.commit()
    conn.close()

init_db()

# Home page
@app.route('/')
def home():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>User Lookup System</title>
            <style>
                body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; }
                input[type="text"] { padding: 10px; width: 300px; }
                button { padding: 10px 20px; background: #007bff; color: white; border: none; cursor: pointer; }
                button:hover { background: #0056b3; }
                .result { margin-top: 20px; padding: 15px; background: #f8f9fa; border-radius: 5px; }
            </style>
        </head>
        <body>
            <h1>User Lookup System</h1>
            <p>Search for users by username:</p>
            <form action="/search" method="GET">
                <input type="text" name="username" placeholder="Enter username">
                <button type="submit">Search</button>
            </form>
        </body>
        </html>
    ''')

# INTENTIONAL VULNERABILITY: SQL Injection
# This endpoint is vulnerable to demonstrate security scanning
@app.route('/search')
def search():
    username = request.args.get('username', '')
    
    # VULNERABLE CODE - DO NOT USE IN PRODUCTION
    # This uses string concatenation instead of parameterized queries
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        
        if results:
            result_html = '<div class="result"><h3>Results:</h3><ul>'
            for user in results:
                result_html += f'<li>ID: {user[0]}, Username: {user[1]}, Email: {user[2]}</li>'
            result_html += '</ul></div>'
        else:
            result_html = '<div class="result"><p>No users found.</p></div>'
            
        return render_template_string('''
            <!DOCTYPE html>
            <html>
            <head>
                <title>Search Results</title>
                <style>
                    body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; }
                    .result { margin-top: 20px; padding: 15px; background: #f8f9fa; border-radius: 5px; }
                    a { color: #007bff; text-decoration: none; }
                </style>
            </head>
            <body>
                <h1>Search Results</h1>
                ''' + result_html + '''
                <p><a href="/">← Back to search</a></p>
            </body>
            </html>
        ''')
    except Exception as e:
        conn.close()
        return f'<h1>Error</h1><p>{str(e)}</p><p><a href="/">Back</a></p>'

# Health check endpoint for container orchestration
@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)