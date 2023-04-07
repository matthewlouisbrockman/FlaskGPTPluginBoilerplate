import yaml

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from flask_apispec import FlaskApiSpec
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

from config import DOMAIN

from no_auth_plugin.game import game, list_games, play_game
from no_auth_plugin.pictures import pictures, generate_picture, generate_picture_get

app = Flask(__name__)
CORS(app)

app.config.update({
  'SEND_FILE_MAX_AGE_DEFAULT':
  0,
  'APISPEC_SPEC':
  APISpec(
    title='Games API',
    version='1.0',
    openapi_version='3.0.2',
    info=dict(description='A great place for games!', ),
    plugins=[MarshmallowPlugin()],
    servers=[{
      "url": DOMAIN,
    }],
  ),
  'APISPEC_SWAGGER_URL':
  '/swagger/',
})
app.register_blueprint(game)
app.register_blueprint(pictures)

spec = FlaskApiSpec(app)
spec.register(list_games, blueprint='game')
spec.register(play_game, blueprint='game')
spec.register(generate_picture, blueprint='pictures')
spec.register(generate_picture_get, blueprint='pictures')

# for debugging purposes, we want to see what chatGPT is sending us in the body / where it's sending it to.
# you shouldn't actually need this and can delete it but heck
@app.before_request
def log_request():
    try:
      print('request to :', request.url, '\n')
      print('request body (if any):', request.get_json(), '\n')
    except:
      print('was not able to parse')
    

@app.route('/')
def index():
  return 'Hello from Flask!'

@app.route('/static/<path:path>')
def send_static(path):
  return send_from_directory('static', path)

@app.route('/artwork/<path:path>')
def send_art(path):
  return send_from_directory('static', path)


# Define a route to serve the OpenAPI specification
@app.route("/.well-known/ai-plugin.json")
def openapi_json():
  my_domain = request.host_url
  print('request to :', my_domain, '\n')
  return jsonify({
    "schema_version": "v1",
    "name_for_human": "Boilerplate Game",
    "name_for_model": "games",
    "description_for_human": "Boilerplate Game Flask App",
    "description_for_model": "Provides rules and options for games.",
    "auth": {
      "type": "none"
    },
    "api": {
      "type": "openapi",
      "url": f"{DOMAIN}openapi.yaml",
      "is_user_authenticated": False
    },
    "logo_url":
    f"{DOMAIN}static/boilerplate.png?1",
    "contact_email": "support@example.com",
    "legal_info_url": "http://www.example.com/legal"
  })


@app.route("/openapi.yaml")
def openapi_yaml():
  openapi_yaml_str = yaml.dump(
    spec.spec.to_dict())  # Convert the specification to YAML
  return openapi_yaml_str, 200, {
    "Content-Type": "text/yaml"
  }  # Return the YAML as plain text

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
