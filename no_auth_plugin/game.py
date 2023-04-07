"""
This is going to be a game that's just kind of random
"""
import uuid
from flask import Blueprint, jsonify
from marshmallow import Schema, fields, ValidationError, validates_schema
from flask_apispec import use_kwargs, marshal_with, doc

from config import DOMAIN

game = Blueprint('game',
                           __name__,
                           url_prefix='/no_auth_game')


class ListGamesResponseSchema(Schema):
  instructions = fields.String()
  games = fields.List(fields.String())


@game.route('play', methods=['GET'])
@doc(description='List games endpoint.', operationId='listGames')
@marshal_with(ListGamesResponseSchema)
def list_games():
  print('play get called')
  #make up a list of games, heck, we'll just say to make them up :P
  return jsonify({'instructions': 'make up a numbered list of text based games'})


class PlayGameRequestSchema(Schema):
  gameId = fields.String()

class CustomPlayGameRequestSchema(Schema):
    gameId = fields.String()
    body = fields.Dict(missing=dict)

    @validates_schema
    def validate_input(self, data, **kwargs):
        if ('gameId' not in data) and ('body' not in data or 'gameId' not in data['body']):
            raise ValidationError('gameId is required in JSON body or within body key')


class PlayGameResponseSchema(Schema):
  instructions = fields.String()
  gameId = fields.String()
  inlineImage: fields.String()

  

@staticmethod
def validate_input(data):
    if ('gameId' not in data) and ('body' not in data or 'gameId' not in data['body']):
        raise ValidationError('gameId is required in JSON body or within body key')


@game.route('play', methods=['POST'])
@use_kwargs(CustomPlayGameRequestSchema, location="json")
@marshal_with(PlayGameResponseSchema)
@doc(description='Play game endpoint.', operationId='playGame',
     tags=['Play Game'],
     consumes=['application/json'])
def play_game(body=None):
  """
  play a game, let the AI figure out what to do next
  """
  print('play post called with body', body )
     
  game_id = body.get('gameId')
  if game_id is None:
    game_id = uuid.uuid4().hex
    return jsonify({
      'instructions':
      'make up how the game should start',
      'gameId':
      game_id,
    })

  return jsonify({
    'instructions': 'make up what happens next',
    'gameId': game_id,
    'inlineImage': f"{DOMAIN}artwork/related_art.png",
  })

