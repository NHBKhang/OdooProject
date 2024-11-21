from odoo import models, fields

class UserLibrary(models.Model):
    _name = 'game.library'
    _inherit = ['mail.thread']
    _description = 'User Game Library'

    name = fields.Char(string='Name', required=True)
    user_id = fields.Many2one(
        'res.users', string="User", required=True,
        help="The user who owns this library.")
    game_ids = fields.Many2many('game.game', string="Games", help="List of games owned by the user.")
