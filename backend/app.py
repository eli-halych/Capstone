from flask import Flask, redirect
from flask_cors import CORS

from controllers import hackathon_api
from models import setup_db
from utils import get_auth0_variables

config_vars = get_auth0_variables()
AUTH0_DOMAIN = config_vars['auth0_domain']
ALGORITHMS = config_vars['algorithms']
API_AUDIENCE = config_vars['api_audience']
CLIENT_ID = config_vars['client_id']
# REDIRECT_URL = config_vars['redirect_url']


def create_app():
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    app.register_blueprint(hackathon_api)

    # @app.route('/')
    # def login():
    #     url = f"https://{AUTH0_DOMAIN}/authorize?" \
    #         f"audience={API_AUDIENCE}" \
    #         f"&response_type=token" \
    #         f"&client_id={CLIENT_ID}" \
    #         f"&redirect_uri={REDIRECT_URL}"
    #     return redirect(url, code=200)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
