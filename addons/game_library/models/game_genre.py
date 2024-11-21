from odoo import models, fields, api

class GameGenre(models.Model):
    _name = 'game.genre'
    _description = 'Game Genre'

    name = fields.Char(string='Genre Name', required=True)