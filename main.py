# This module runs the website
from website import create_app

app = create_app()

# This make sure python only runs this website
if __name__ == '__main__':
    app.run(debug=True)
