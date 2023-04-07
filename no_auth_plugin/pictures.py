"""
This is going to be a game that's just kind of random
"""
from flask import Blueprint, jsonify, request
from marshmallow import Schema, fields, ValidationError, validates_schema
from flask_apispec import use_kwargs, marshal_with, doc

from utils.gpt_user import parse_user_info
from config import DOMAIN

pictures = Blueprint('pictures',
                           __name__,
                           url_prefix='/pictures')


class ArtRequestSchema(Schema):
  pictureDescription = fields.String()
  urlImHitting = fields.String()
  body = fields.Dict(missing=dict)

  @validates_schema
  def validate_input(self, data, **kwargs):
      print('GOT DATA FOR PICTUREDESCriPTION: ', data)
      if ('pictureDescription' not in data) and ('body' not in data or 'pictureDescription' not in data['body']):
          raise ValidationError('wait i dont need gameId')

class ArtResponseSchema(Schema):
  inlineImage = fields.String(
      metadata={'description': 'the image that matches the request'})
  
@pictures.route('generate_picture', methods=['POST'])
@use_kwargs(ArtRequestSchema, location="json")
@marshal_with(ArtResponseSchema)
@doc(description='Generate picture POST endpoint.', operationId='generatePicturePOST',
      tags=['Generate Picture'],
      consumes=['application/json'])
def generate_picture(body=None, **_):
  """
  Generate a picture based on the description
  """
  headers = request.headers
  user_info = parse_user_info(headers)
  print('generate picture post called with body', body, ' by ', user_info )
  return jsonify({
    'inlineImage':f"{DOMAIN}artwork/related_art.png",
  })
   

class ArtGetSchema(Schema):
  pictureDescription = fields.String()

# take the pictureDescription as a GET query
@pictures.route('generate_picture', methods=['GET'])
@use_kwargs(ArtGetSchema, location="query")
@marshal_with(ArtResponseSchema)
@doc(description='Generate picture GET endpoint.', operationId='generatePictureGET',
      tags=['Generate Picture'],  
      consumes=['application/json'])

def generate_picture_get(pictureDescription=None, **_):
  """
  Generate a picture based on the description
  """
  headers = request.headers
  user_info = parse_user_info(headers)

  print('generate picture get called with pictureDescription', pictureDescription, ' by ', user_info )
  return jsonify({
    'inlineImage':f"{DOMAIN}artwork/related_art.png",
  })

