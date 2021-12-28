import uvicorn
from YCU_Supervisory_System import app

if __name__ == '__main__':
    # uvicorn.run(app, host='0.0.0.0', port=8000)
    uvicorn.run('YCU_Supervisory_System:app', host='0.0.0.0', port=8194, reload=True, debug=True)
