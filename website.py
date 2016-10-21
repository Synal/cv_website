from app import app
# import sys

# reload(sys)
# sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='0.0.0.0', port=5005, threaded=True)
