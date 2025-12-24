"""
Flask web application for notes management
"""
import os
from datetime import datetime
from flask import Flask, render_template_string, request, jsonify
import psycopg2
from psycopg2 import pool

app = Flask(__name__)

# Connection pool for better performance
db_pool = None


def init_db_pool():
    """Initialize database connection pool"""
    global db_pool
    try:
        db_pool = psycopg2.pool.SimpleConnectionPool(
            1, 10,
            host=os.environ.get('DB_HOST', 'db'),
            database=os.environ.get('DB_NAME', 'notesdb'),
            user=os.environ.get('DB_USER', 'postgres'),
            password=os.environ.get('DB_PASSWORD', 'postgres'),
            port=os.environ.get('DB_PORT', '5432')
        )
        print("✓ Database pool created successfully")
    except Exception as error:
        print(f"✗ Error creating database pool: {error}")


def get_connection():
    """Get connection from pool"""
    if db_pool:
        return db_pool.getconn()
    return None


def release_connection(conn):
    """Return connection to pool"""
    if db_pool and conn:
        db_pool.putconn(conn)


HOME_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notes App - DevOps Lab</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            padding: 40px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }
        h1 {
            color: #667eea;
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        .subtitle {
            color: #666;
            margin-bottom: 30px;
            font-size: 1.1em;
        }
        .info-box {
            background: #f8f9fa;
            border-left: 4px solid #667eea;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
        }
        .api-section {
            margin-top: 30px;
        }
        .endpoint {
            background: #fff;
            border: 2px solid #e9ecef;
            padding: 15px;
            margin: 10px 0;
            border-radius: 8px;
            transition: all 0.3s;
        }
        .endpoint:hover {
            border-color: #667eea;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102,126,234,0.2);
        }
        .method {
            display: inline-block;
            padding: 5px 12px;
            border-radius: 4px;
            font-weight: bold;
            margin-right: 10px;
            font-size: 0.85em;
        }
        .get { background: #28a745; color: white; }
        .post { background: #007bff; color: white; }
        .path {
            font-family: 'Courier New', monospace;
            color: #495057;
            font-weight: 600;
        }
        .description {
            color: #6c757d;
            margin-top: 8px;
            font-size: 0.95em;
        }
        footer {
            margin-top: 40px;
            text-align: center;
            color: #999;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📝 Notes Application</h1>
        <p class="subtitle">DevOps Laboratory work with Docker & PostgreSQL</p>
        
        <div class="info-box">
            <strong>🚀 Status:</strong> Application is running successfully!<br>
            <strong>🗄️ Database:</strong> PostgreSQL connected
        </div>

        <div class="api-section">
            <h2>📡 Available API Endpoints</h2>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <span class="path">/</span>
                <div class="description">Home page with documentation</div>
            </div>

            <div class="endpoint">
                <span class="method get">GET</span>
                <span class="path">/health</span>
                <div class="description">Health check endpoint for monitoring</div>
            </div>

            <div class="endpoint">
                <span class="method get">GET</span>
                <span class="path">/api/notes</span>
                <div class="description">Retrieve all notes from database</div>
            </div>

            <div class="endpoint">
                <span class="method post">POST</span>
                <span class="path">/api/notes</span>
                <div class="description">Create a new note (JSON body required)</div>
            </div>
        </div>

        <footer>
            <p>Created with ❤️ for DevOps course | 2024</p>
        </footer>
    </div>
</body>
</html>
"""


@app.route('/')
def index():
    """Main page"""
    return render_template_string(HOME_TEMPLATE)


@app.route('/health')
def health_check():
    """Health check endpoint"""
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT 1')
            cursor.close()
            release_connection(conn)
            return jsonify({
                'status': 'healthy',
                'database': 'connected',
                'timestamp': datetime.now().isoformat()
            }), 200
        except Exception as e:
            release_connection(conn)
            return jsonify({
                'status': 'unhealthy',
                'database': 'error',
                'error': str(e)
            }), 503
    return jsonify({
        'status': 'unhealthy',
        'database': 'disconnected'
    }), 503


@app.route('/api/notes', methods=['GET'])
def list_notes():
    """Get all notes"""
    conn = get_connection()
    if not conn:
        return jsonify({'error': 'Database unavailable'}), 503
    
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, title, content, created_at, updated_at 
            FROM notes 
            ORDER BY created_at DESC
        ''')
        
        columns = ['id', 'title', 'content', 'created_at', 'updated_at']
        results = []
        for row in cursor.fetchall():
            note = dict(zip(columns, row))
            note['created_at'] = note['created_at'].isoformat() if note['created_at'] else None
            note['updated_at'] = note['updated_at'].isoformat() if note['updated_at'] else None
            results.append(note)
        
        cursor.close()
        release_connection(conn)
        
        return jsonify({
            'success': True,
            'count': len(results),
            'data': results
        }), 200
    except Exception as e:
        release_connection(conn)
        return jsonify({'error': str(e)}), 500


@app.route('/api/notes', methods=['POST'])
def create_note():
    """Create new note"""
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    title = data.get('title', '').strip()
    content = data.get('content', '').strip()
    
    if not title or not content:
        return jsonify({'error': 'Title and content are required'}), 400
    
    conn = get_connection()
    if not conn:
        return jsonify({'error': 'Database unavailable'}), 503
    
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO notes (title, content) 
            VALUES (%s, %s) 
            RETURNING id, title, content, created_at, updated_at
        ''', (title, content))
        
        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        release_connection(conn)
        
        note = {
            'id': result[0],
            'title': result[1],
            'content': result[2],
            'created_at': result[3].isoformat() if result[3] else None,
            'updated_at': result[4].isoformat() if result[4] else None
        }
        
        return jsonify({
            'success': True,
            'message': 'Note created successfully',
            'data': note
        }), 201
    except Exception as e:
        conn.rollback()
        release_connection(conn)
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    init_db_pool()
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('APP_PORT', 5000)),
        debug=os.environ.get('FLASK_ENV') == 'development'
    )