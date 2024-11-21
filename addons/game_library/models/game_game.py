import random
import string

from odoo import models, fields, api

class Game(models.Model):
    _name = 'game.game'
    _inherit = ['mail.thread']
    _description = 'Game Management'

    number = fields.Char(string='Game Number', required=True, copy=False, readonly=True, default='New')
    cover = fields.Image(string='Cover Image', required=False)
    name = fields.Char(string="Game Name", required=True)
    description = fields.Text(string="Description")
    genre_ids = fields.Many2many('game.genre', string="Genres")
    release_date = fields.Date(string="Release Date")
    price = fields.Float(string="Price", required=True)
    currency_id = fields.Many2one(
        'res.currency', string="Currency", default=lambda self: self.env.company.currency_id)
    developer = fields.Char(string="Developer")
    publisher = fields.Char(string="Publisher")

    @api.depends('release_date')
    def _compute_release_month(self):
        for record in self:
            if record.release_date:
                record.release_month = fields.Date.from_string(record.release_date).month
            else:
                record.release_month = 0

    @api.depends('release_date')
    def _compute_release_year(self):
        for record in self:
            if record.release_date:
                record.release_year = fields.Date.from_string(record.release_date).year
            else:
                record.release_year = 0

    @api.model_create_multi
    def create(self, vals_list):
        if not isinstance(vals_list, list):
            vals_list = [vals_list]

        for vals in vals_list:
            if not vals.get('number'):
                vals['number'] = f"{''.join(random.choices(string.ascii_uppercase, k=4))}-{''.join(random.choices(string.digits, k=4))}"

        return super(Game, self).create(vals_list)

    @api.model
    def get_release_statistics(self):
        games = self.search([])
        statistics = defaultdict(lambda: 0)

        for game in games:
            if game.release_date:
                release_date = datetime.strptime(game.release_date, "%Y-%m-%d")
                key = (release_date.year, release_date.month)
                statistics[key] += 1

        result = [{'year': year, 'month': month, 'count': count} for (year, month), count in statistics.items()]
        result.sort(key=lambda x: (x['year'], x['month']))
        return result
